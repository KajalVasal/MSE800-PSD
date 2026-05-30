
# ===== Base Parent Class =====
class Flight:
    def __init__(self, flight_no, airline, origin, destination):
        # Shared attributes - inherited by all subclasses
        self.flight_no = flight_no
        self.airline = airline
        self.origin = origin
        self.destination = destination

    # Method 1: Shared method
    def show_info(self):
        """Display basic flight info"""
        return f"{self.airline} {self.flight_no}: {self.origin} -> {self.destination}"

    # Method 2: Shared method
    def get_route(self):
        """Return route details"""
        return f"Route: {self.origin} to {self.destination}"

    # Method 3: Shared method
    def delay_flight(self, minutes):
        """Delay flight by minutes"""
        return f"Flight {self.flight_no} delayed by {minutes} min"

# ===== Intermediate Child 1: Single inheritance =====
class DomesticFlight(Flight):
    def __init__(self, flight_no, airline, origin, destination, baggage_kg, terminal):
        # Explicit call to avoid super() MRO issue in hybrid inheritance
        Flight.__init__(self, flight_no, airline, origin, destination)
        
        # Domestic-specific attributes
        self.baggage_kg = baggage_kg
        self.terminal = terminal

    # Method 1: New method specific to domestic
    def check_baggage(self, weight):
        """Check baggage against NZ domestic limit 23kg"""
        if weight <= self.baggage_kg:
            return f"OK: {self.baggage_kg - weight}kg remaining"
        return f"Overweight by {weight - self.baggage_kg}kg. Fee applies"

    # Method 2: New method specific to domestic
    def gate_info(self):
        """Return terminal/gate info"""
        return f"Proceed to {self.terminal}"

    # Method 3: Override parent method
    def show_info(self):
        """Extend parent show_info with domestic details"""
        base = Flight.show_info(self)  # explicit call
        return f"{base} | Type: Domestic | Terminal: {self.terminal}"

# ===== Intermediate Child 2: Single inheritance =====
class InternationalFlight(Flight):
    def __init__(self, flight_no, airline, origin, destination, passport_req, visa_req):
        # Explicit call to avoid super() MRO issue
        Flight.__init__(self, flight_no, airline, origin, destination)
        
        # International-specific attributes
        self.passport_required = passport_req
        self.visa_required = visa_req

    # Method 1: New method specific to international
    def check_passport(self):
        """Check if passport is required"""
        return "Passport required" if self.passport_required else "No passport needed"

    # Method 2: New method specific to international
    def check_visa(self):
        """Check if visa is required"""
        return "Visa required" if self.visa_required else "No visa required"

    # Method 3: Override parent method
    def show_info(self):
        """Extend parent show_info with international details"""
        base = Flight.show_info(self)
        visa = "Visa Yes" if self.visa_required else "Visa No"
        return f"{base} | Type: International | {visa}"

# ===== Hybrid Child: Multiple inheritance =====
class AirNZFlight(DomesticFlight, InternationalFlight):
    def __init__(self, flight_no, airline, origin, destination, baggage_kg, terminal, passport, visa, flight_type):
        # Explicitly call both parents to initialize all attributes
        # This fixes the TypeError you got with super()
        DomesticFlight.__init__(self, flight_no, airline, origin, destination, baggage_kg, terminal)
        InternationalFlight.__init__(self, flight_no, airline, origin, destination, passport, visa)
        
        # Hybrid-specific attribute
        self.flight_type = flight_type

    # Method 1: New method combining both parents
    def full_check(self, weight, has_passport):
        """Run baggage check from Domestic + passport check from International"""
        b_status = self.check_baggage(weight)
        p_status = self.check_passport() if has_passport else "Passport missing"
        return f"Baggage Check: {b_status} | Passport Check: {p_status}"

    # Method 2: Final override for hybrid class
    def show_info(self):
        """Final version for AirNZFlight"""
        return f"{self.airline} {self.flight_no} | {self.flight_type} | {self.origin} -> {self.destination}"

    # Method 3: New method using inherited methods
    def get_status(self):
        """Get full flight status using inherited gate_info"""
        return f"Flight {self.flight_no} is on schedule. {self.gate_info()}"