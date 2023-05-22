# ========== CREATING VEHICLE HIERARCHY =========
class Vehicle:
    def __init__(self, v_make, v_model, v_year):
        self.v_make = v_make
        self.v_model = v_model
        self.v_year = v_year

        


display_info = Vehicle("Ranger", "2000", "2023")
print(display_info.v_make, display_info.v_model, display_info.v_year)

class Car(Vehicle):
    def __init__(self, v_make, v_model, v_year, v_color):
        super().__init__(v_make, v_model, v_year)
        self.color = v_color


display_info = Car("Ferari", "200", "2023", "Blue")
print(display_info.v_make, display_info.v_model, display_info.v_year, display_info.color)
    
# ========== CREATING A SHAPE HIERARCHY ==========
class Shape:
    def __init__(self, s_color) -> None:
        self.color = s_color

display_info = Shape("blue")



class Circle(Shape):
    def __init__(self, s_color, radius) -> None:
        self.color = super().__init__(s_color)        
        self.radius = radius

