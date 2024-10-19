create database ManteMaquinaria2;
use ManteMaquinaria2;

-- drop database ManteMaquinaria2;
-- tablas sin foreanea
SET SQL_SAFE_UPDATES = 0;
create table empleados(
id_empleado int auto_increment primary key,
nombre_empleado varchar(50),
apellidoMaterno_empleado varchar(50),
apellidoPaterno_empleado varchar(50),
telefono double,
correo varchar(50)
);

create table proveedor_piezas (
id_proveedor_piezas int auto_increment primary key,
Nombre_empresa varchar(100),
RFC varchar(40),
fecha_registro date,
tipo_moneda_pago enum ('Moneda Mexicana','Moneda Americana') Default 'Moneda americana' NOT NULL
);

create table piezas(
id_pieza int auto_increment primary key,
nombre_pieza varchar(50),
precio double,
descripcion varchar(50)
);

create table Areas(
id_areas int auto_increment primary key,
tipo varchar (30) -- 
);

create table maquinaria (
id_maquinaria int auto_increment primary key,
nombre_maquinaria varchar(100),
modelo varchar(100),
marca varchar(50),
fecha_adquisicion date,
estado varchar(50)
);

create table empresas(
id_empresa int auto_increment primary key,
nombre_empresa  varchar(100),
ubicacion_empresa varchar(100),
RFC varchar(50)
);

create table DetalleMaquinaria_empresa(
id_detalle_maquinaria_empresa int primary key auto_increment,
id_empresa int,
id_maquinaria int,
foreign key (id_empresa) references empresas (id_empresa),
foreign key (id_maquinaria) references maquinaria(id_maquinaria)
);

-- registrar ingresas obtenidos por realizar mantenimientos a empresas
create table tipo_mantenimiento (
id_tipo_mantenimiento int auto_increment primary key,
nombre_tipo_mantenimiento varchar(100),
descripcion varchar(100),
precio double,
fecha_servicio date
);

create table mantenimientos(
id_mantenimiento int auto_increment primary key,
id_empresa int,
id_maquinaria int,
id_tipo_mantenimiento int,
Responsable_mantenimiento int,
fecha_programada date,
fecha_realizacion date,
descripcion varchar (50),
foreign key (id_empresa) references empresas(id_empresa),
foreign key (id_maquinaria) references maquinaria(id_maquinaria),
foreign key (id_tipo_mantenimiento) references tipo_mantenimiento(id_tipo_mantenimiento),
foreign key (Responsable_mantenimiento) references empleados(id_empleado)

);

create table piezas_mantenimiento(
ind_pieza_mantenimiento int auto_increment primary key,
id_mantenimiento int, -- fk
id_pieza int, -- fk
cantidad_usada int,
foreign key (id_mantenimiento) references mantenimientos(id_mantenimiento),
foreign key (id_pieza) references piezas(id_pieza)
);

create table reparaciones(
id_reparacion int auto_increment primary key,
id_maquinaria int,
fecha_reparacion date,
descripcion varchar(100),
costo double,
foreign key (id_maquinaria) references maquinaria(id_maquinaria)
);

create table historial_maquinas(
id_historial int auto_increment primary key,
id_maquinaria int, -- fk
tipo_evento varchar(100),
fecha_evento date,
descripcion_evento varchar(150),
foreign key (id_maquinaria) references maquinaria(id_maquinaria)
);

create table inicio_sesion(
id_usuario int primary key,
id_areas int,
usuario varchar(50),
contraseña varchar(50),
foreign key (id_usuario) references empleados(id_empleado),
foreign key (id_areas) references Areas(id_areas)
);


-- tablas con llaves foraneas
create table add_pieza (
id_add_pieza int auto_increment primary key,
id_pieza int,
id_proveedor int,
cantidad_piezas int,
descripcion_pieza varchar(50),
foreign key (id_pieza) references piezas(id_pieza),
foreign key (id_proveedor) references proveedor_piezas(id_proveedor_piezas)
);

create table inventario_piezas(
id_inventario int auto_increment primary key,
cantidad_stock_piezas int NOT NULL,
id_pieza int NOT NULL,
fecha_entrada date,
foreign key (id_pieza) references piezas(id_pieza)
);

create table ganancias(
id_ganancia int auto_increment primary key,
id_reparacion int,
ingresos double default 0,
fecha date,
foreign key (id_reparacion) references reparaciones(id_reparacion)
);

CREATE TABLE banco_em (
    id_banco INT AUTO_INCREMENT PRIMARY KEY,
    dinero DOUBLE DEFAULT 0
);


-- disparadores

-- modifica el stock en siempre y cuando exista dinero disponible en el banco
DELIMITER //

CREATE TRIGGER Tr_StockBanco
AFTER INSERT ON add_pieza
FOR EACH ROW
BEGIN
    DECLARE costo_total DOUBLE;
    DECLARE nuevo_saldo DOUBLE;

    -- Obtener el costo total de la compra
    SELECT precio INTO costo_total
    FROM piezas
    WHERE id_pieza = NEW.id_pieza;

    SET costo_total = costo_total * NEW.cantidad_piezas;

    -- Calcular el nuevo saldo potencial en banco_em
    SELECT dinero - costo_total INTO nuevo_saldo
    FROM banco_em;

    -- Verificar si el nuevo saldo será negativo
    IF nuevo_saldo < 0 THEN
        -- Si el saldo será negativo, lanzar un error
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: No se puede comprar pieza, saldo insuficiente en banco';
    ELSE
        -- Si el saldo es suficiente, hacer la actualización
        UPDATE banco_em
        SET dinero = nuevo_saldo;
        
        -- Actualizar el inventario de piezas
        UPDATE inventario_piezas
        SET cantidad_stock_piezas = cantidad_stock_piezas + NEW.cantidad_piezas
        WHERE id_pieza = NEW.id_pieza;
    END IF;

END;
//
DELIMITER ;



-- disparador que aumente las cifras en ganancias simpre y si no existe un registro con ese id_reparacion lo agrega como nuevo registro
DELIMITER //

CREATE TRIGGER Tr_AumDinG AFTER INSERT ON reparaciones
FOR EACH ROW
BEGIN
    DECLARE v_id_reparacion INT;
    DECLARE v_costo DOUBLE;

    -- Capturar los valores de la nueva reparación
    SET v_id_reparacion = NEW.id_reparacion;
    SET v_costo = NEW.costo;

    -- Verificar si existe un registro de ganancia asociado al id_reparacion
    IF (SELECT COUNT(*) FROM ganancias WHERE id_reparacion = v_id_reparacion) > 0 THEN
        -- Si existe, sumar el costo de la reparación al ingreso
        UPDATE ganancias
        SET ingresos = ingresos + v_costo
        WHERE id_reparacion = v_id_reparacion;
    ELSE
        -- Si no existe, insertar un nuevo registro en la tabla ganancias
        INSERT INTO ganancias (id_reparacion, ingresos, fecha)
        VALUES (v_id_reparacion, v_costo, CURDATE());
    END IF;
END;
//
DELIMITER ;

-- aumenta el total de dinero respecto a las ganancias obtenidas en ganancias, suma en banco
DELIMITER //

CREATE TRIGGER Tr_ActDinero
AFTER INSERT ON ganancias
FOR EACH ROW
BEGIN
    -- Actualizar el saldo total de dinero en banco_em
    UPDATE banco_em
    SET dinero = dinero + NEW.ingresos
    WHERE id_banco = 1;  -- Suponiendo que solo tienes un registro en banco_em
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER Tr_AgregarInventario
AFTER INSERT ON piezas
FOR EACH ROW
BEGIN
    -- Insertar un nuevo registro en inventario_piezas
    INSERT INTO inventario_piezas (cantidad_stock_piezas, id_pieza, fecha_entrada)
    VALUES (0, NEW.id_pieza, CURDATE()); -- Inicializa la cantidad de stock en 0
END;
//
DELIMITER ;

-- Reduce inventario piezas siempre y cuando el inventario cuente con stock para realizar los mantenimientos
DELIMITER //

CREATE TRIGGER Tr_DisExiInvP
AFTER INSERT ON piezas_mantenimiento
FOR EACH ROW
BEGIN
    DECLARE v_id_pieza INT;
    DECLARE v_cantidad_usada INT;
    DECLARE v_stock_actual INT;

    SET v_id_pieza = NEW.id_pieza;
    SET v_cantidad_usada = NEW.cantidad_usada;

    -- Obtener el stock actual
    SELECT cantidad_stock_piezas INTO v_stock_actual
    FROM inventario_piezas
    WHERE id_pieza = v_id_pieza;

    -- Verificar si hay suficiente stock
    IF v_stock_actual < v_cantidad_usada THEN
        -- Si no hay suficiente stock, lanzar un error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Stock insuficiente para realizar la operación.';
    ELSE
        -- Actualizar el stock si hay suficiente
        UPDATE inventario_piezas
        SET cantidad_stock_piezas = cantidad_stock_piezas - v_cantidad_usada
        WHERE id_pieza = v_id_pieza;
    END IF;
END;
//

DELIMITER ;

-- insert de 
INSERT INTO empleados (nombre_empleado, apellidoMaterno_empleado, apellidoPaterno_empleado, telefono, correo)
VALUES ('Juan', 'Pérez', 'García', 1234567890, 'juan.perez@example.com');
INSERT INTO proveedor_piezas (Nombre_empresa, RFC, fecha_registro, tipo_moneda_pago)
VALUES ('Proveedores de Maquinaria S.A.', 'RFC123456789', '2024-01-01', 'Moneda Mexicana');
INSERT INTO Areas (tipo)
VALUES ('Mantenimiento');
-- Dinero total de la empresa
INSERT INTO banco_em (dinero) 
VALUES (0); 
-- Acciones para la gestion de las maquinas
INSERT INTO piezas (nombre_pieza, precio, descripcion)
VALUES ('Motor de Excavadora', 150.00, 'Motor para excavadora CAT 320D');
INSERT INTO maquinaria (nombre_maquinaria, modelo, marca, fecha_adquisicion, estado)
VALUES ('Excavadora CAT 320D', 'CAT320D', 'Caterpillar', '2023-05-15', 'Operativa');
INSERT INTO maquinaria (nombre_maquinaria, modelo, marca, fecha_adquisicion, estado)
VALUES ('Excavadora C2D', 'C2D', 'Catillar', '2023-06-13', 'Operativa');

INSERT DetalleMaquinaria_empresa (id_empresa,id_maquinaria) 
VALUES (1,1);
INSERT DetalleMaquinaria_empresa (id_empresa,id_maquinaria) 
VALUES (1,2);

-- Datos de la empresa a las que se le haran el mantenimiento
INSERT INTO empresas (nombre_empresa, ubicacion_empresa, RFC)
VALUES ('Construcciones XYZ', 'Calle Falsa 123', 'RFCXYZ123456');

INSERT INTO tipo_mantenimiento (nombre_tipo_mantenimiento, descripcion, precio, fecha_servicio)
VALUES ('Mantenimiento Preventivo', 'Mantenimiento regular para maquinaria', 2000.00, '2024-02-01');

INSERT INTO mantenimientos (id_empresa, id_maquinaria, id_tipo_mantenimiento, Responsable_mantenimiento, fecha_programada, fecha_realizacion, descripcion)
VALUES (1, 1, 1, 1, '2024-02-10', '2024-02-11', 'Mantenimiento preventivo de excavadora');
--
-- Tabla en la que se va a hacer la relacion de cuando un mantenimiento esta realizado y el costo añadido se suma en el banco de la empresa
INSERT INTO reparaciones (id_maquinaria, fecha_reparacion, descripcion, costo)
VALUES (1, '2024-03-01', 'Reparación de motor', 5000.00);
-- Drop database ManteMaquinaria2;
INSERT INTO add_pieza (id_pieza, id_proveedor, cantidad_piezas, descripcion_pieza)
VALUES (1, 1, 10, 'Compra de piezas para mantenimiento de excavadora');
-- Tabla para utilizar piezas para realizar mantenimientos
INSERT INTO piezas_mantenimiento (id_mantenimiento, id_pieza, cantidad_usada)
VALUES (1, 1, 5);

INSERT INTO historial_maquinas (id_maquinaria, tipo_evento, fecha_evento, descripcion_evento)
VALUES (1, 'Mantenimiento', '2024-02-12', 'Se realizó mantenimiento preventivo');
-- tabla para asignar un inicio de sesion al usuario agregado
-- 
INSERT INTO inicio_sesion (id_usuario, id_areas, usuario, contraseña)
VALUES (1, 1, 'juangarcia', 'password123');






























