# class LedLamp:
#     def __init__(self):
#         self.turned_on = False
#
#     def turn_on(self):
#         self.turned_on = True
#         print("LED lamp is turned on.")
#
#     def turn_off(self):
#         self.turned_on = False
#         print("LED lamp is turned off.")
#
# class KsenonLamp:
#     def __init__(self):
#         self.turned_on = False
#
#     def turn_on(self):
#         self.turned_on = True
#         print("Ksenon lamp is turned on.")
#
#     def turn_off(self):
#         self.turned_on = False
#         print("Ksenon lamp is turned off.")
#
#
# class LightSwitch:
#     def __init__(self, ):
#         self.lamp = LedLamp()
#
#     def switch_light(self):
#         if not self.lamp.turned_on:
#             return self.lamp.turn_on()
#         else:
#             return self.lamp.turn_off()
#
# class KsenonLightSwitch:
#     def __init__(self):
#         self.lamp = KsenonLamp()
#
#     def switch_light(self):
#         if not self.lamp.turned_on:
#             return self.lamp.turn_on()
#         else:
#             return self.lamp.turn_off()
#
#
# switch = LightSwitch()
#
# switch.switch_light()  # Turns on the LED lamp
# switch.switch_light()  # Turns off the LED lamp

from abc import ABC, abstractmethod
class LightSource(ABC):

    def __init__(self):
        self.turned_on = False

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Switch:

    def __init__(self, light_source: LightSource):
        self.light_source = light_source


    def switch_light(self):
        if not self.light_source.turned_on:
            return self.light_source.turn_on()
        else:
            return self.light_source.turn_off()


class KsenonLamp(LightSource):

    def turn_on(self):
        self.turned_on = True
        print("Ksenon lamp is turned on.")

    def turn_off(self):
        self.turned_on = False
        print("Ksenon lamp is turned off.")

class LedLamp(LightSource):
    def turn_on(self):
        self.turned_on = True
        print("LED lamp is turned on.")

    def turn_off(self):
        self.turned_on = False
        print("LED lamp is turned off.")


class HalogenLamp(LightSource):
    def turn_on(self):
        self.turned_on = True
        print("Halogen lamp is turned on.")

    def turn_off(self):
        self.turned_on = False
        print("Halogen lamp is turned off.")

switch1 = Switch(LedLamp())
switch2 = Switch(KsenonLamp())
switch3 = Switch(HalogenLamp())

switch1.switch_light()  # Turns on the LED lamp
switch1.switch_light()  # Turns off the LED lamp
switch2.switch_light()  # Turns on the Ksenon lamp
switch2.switch_light()  # Turns off the Ksenon lamp
switch3.switch_light()  # Turns on the Halogen lamp
switch3.switch_light()  # Turns off the Halogen lamp
