import logging
from abc import ABC, abstractmethod

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str, spec: str) -> None:
        super().__init__(make, model, spec)

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, spec: str) -> None:
        super().__init__(make, model, spec)

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()
