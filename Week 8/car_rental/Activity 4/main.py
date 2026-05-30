
from flight import Flight, DomesticFlight, InternationalFlight, AirNZFlight

def main():

    print(" HYBRID INHERITANCE")
    
    
    # TEST 1: Domestic Flight only - Single inheritance
    print("TEST 1: DomesticFlight Object - Single Inheritance")
    d1 = DomesticFlight("NZ501", "Air New Zealand", "Auckland", "Wellington", 23, "Domestic Terminal")
    print(f"1. Inherited show_info: {d1.show_info()}")
    print(f"2. Inherited get_route: {d1.get_route()}")
    print(f"3. Own method check_baggage 20kg: {d1.check_baggage(20)}")
    print(f"4. Inherited delay_flight: {d1.delay_flight(10)}\n")
    
    # TEST 2: International Flight only - Single inheritance
    print("TEST 2: InternationalFlight Object - Single Inheritance")
    i1 = InternationalFlight("NZ2", "Air New Zealand", "Auckland", "Los Angeles", True, True)
    print(f"1. Overridden show_info: {i1.show_info()}")
    print(f"2. Own method check_passport: {i1.check_passport()}")
    print(f"3. Own method check_visa: {i1.check_visa()}\n")
    
    # TEST 3: Hybrid Flight - Multiple + Single inheritance
    print("TEST 3: AirNZFlight Hybrid Object - Hybrid Inheritance")
    h1 = AirNZFlight(
        flight_no="NZ123",
        airline="Air New Zealand",
        origin="Auckland AKL",
        destination="Sydney SYD",
        baggage_kg=23,
        terminal="International Terminal",
        passport=True,
        visa=True,
        flight_type="Trans-Tasman"
    )
    
    print("A. Inherited from Flight parent class:")
    print(f"   Route: {h1.get_route()}")
    print(f"   Delay: {h1.delay_flight(30)}")
    
    print("\nB. Inherited from DomesticFlight:")
    print(f"   Gate: {h1.gate_info()}")
    print(f"   Baggage 22kg: {h1.check_baggage(22)}")
    print(f"   Baggage 27kg: {h1.check_baggage(27)}")
    
    print("\nC. Inherited from InternationalFlight:")
    print(f"   Passport: {h1.check_passport()}")
    print(f"   Visa: {h1.check_visa()}")
    
    print("\nD. Hybrid class AirNZFlight methods:")
    print(f"   Full Check: {h1.full_check(24, True)}")
    print(f"   Show Info: {h1.show_info()}")
    print(f"   Status: {h1.get_status()}")
    
    print("\nE. Inheritance Proof:")
    print(f"   isinstance h1 -> Flight: {isinstance(h1, Flight)}")
    print(f"   isinstance h1 -> DomesticFlight: {isinstance(h1, DomesticFlight)}")
    print(f"   isinstance h1 -> InternationalFlight: {isinstance(h1, InternationalFlight)}")
    print(f"   MRO: {[cls.__name__ for cls in AirNZFlight.__mro__]}")
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()