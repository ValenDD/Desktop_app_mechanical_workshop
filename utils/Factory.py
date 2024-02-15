from controllers import client_controller
from controllers import dao_controller
from controllers import work_controller
class Factory:
    _instance = None
    _controllers = {}
    _controller_classes = {
        'clientController': client_controller.ClientController,
        'DAOcontroller': dao_controller.DAOcontroller,
        'workController': work_controller.WorkController,
    }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Factory, cls).__new__(cls)
        return cls._instance

    def get_controller(self, controller_name, *args, **kwargs):
        if controller_name not in self._controllers:
            # Obtener la clase del diccionario usando el nombre como clave
            controller_class = self._controller_classes[controller_name]
            # Crear una instancia de la clase del controlador
            self._controllers[controller_name] = controller_class(*args, **kwargs)
        return self._controllers[controller_name]
    