import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, sensor
from esphome.const import CONF_ID, CONF_NAME

CODEOWNERS = ["@MichaelBitard"]
DEPENDENCIES = ["uart"]

toshiba_controller_ns = cg.esphome_ns.namespace("toshiba_controller")
ToshibaController = toshiba_controller_ns.class_("ToshibaController", cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ToshibaController),
    cv.Optional(CONF_NAME, default="Toshiba Climate"): cv.string,
}).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
    cg.add(var.set_name(config[CONF_NAME]))
    cg.add(cg.App.register_climate(var))
