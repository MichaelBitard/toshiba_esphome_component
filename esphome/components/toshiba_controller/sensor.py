import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import UNIT_EMPTY, ICON_EMPTY

empty_sensor_ns = cg.esphome_ns.namespace("toshiba_controller")
EmptySensor = empty_sensor_ns.class_("ToshibaController", cg.PollingComponent)

CONFIG_SCHEMA = sensor.sensor_schema(
    EmptySensor,
    unit_of_measurement=UNIT_EMPTY,
    icon=ICON_EMPTY,
    accuracy_decimals=1,
).extend(cv.polling_component_schema("60s"))


async def to_code(config):
    var = await sensor.new_sensor(config)
    await cg.register_component(var, config)


#
#
# import esphome.codegen as cg
# import esphome.config_validation as cv
# from esphome.components import uart, sensor
# from esphome.const import CONF_ID, CONF_NAME
#
# CODEOWNERS = ["@MichaelBitard"]
# DEPENDENCIES = ["uart"]
#
# toshiba_controller_ns = cg.esphome_ns.namespace("toshiba_controller")
# ToshibaController = toshiba_controller_ns.class_("ToshibaController", cg.Component)
#
# CONFIG_SCHEMA = cv.Schema({
#     cv.GenerateID(): cv.declare_id(ToshibaController),
#     cv.Optional(CONF_NAME, default="Toshiba Climate"): cv.string,
# }).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)
#
# async def to_code(config):
#     var = cg.new_Pvariable(config[CONF_ID])
#     await cg.register_component(var, config)
#     await uart.register_uart_device(var, config)
#     cg.add(var.set_name(config[CONF_NAME]))
#     cg.add(cg.App.register_climate(var))
