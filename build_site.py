#!/usr/bin/env python3
"""Generate Lockout Pro SWFL — automotive + residential lockouts."""

from pathlib import Path
from datetime import date
import json

ROOT = Path(__file__).resolve().parent
DOMAIN = "https://lockoutproswfl.com"
PHONE_DISPLAY = "(239) 380-5240"
PHONE_TEL = "2393805240"
PHONE_SCHEMA = "+1-239-380-5240"
BRAND = "Lockout Pro SWFL"
TODAY = date.today().isoformat()
AGL = "https://agoodlocksmith.com"


AREA_DETAILS = {
    "fort-myers": {
        "blurb": "Fort Myers is a central hub for Southwest Florida drivers and residents — downtown corridors, residential neighborhoods, medical campuses, and retail lots where lockouts happen every week.",
        "vehicle": "From downtown parking to Colonial Boulevard errands, Fort Myers car and SUV lockouts are one of our most common calls. If keys are locked inside, call and we will come to you.",
        "home": "Home, apartment, and condo lockouts happen across Fort Myers neighborhoods day and night. Share your address and we will give a realistic arrival estimate.",
        "nearby": ["cape-coral", "north-fort-myers", "lehigh-acres", "san-carlos-park"],
        "links": [("Car Lockouts in Fort Myers", "/services/car-lockouts/"), ("Home Lockouts", "/services/home-lockouts/"), ("Keys Locked In Car", "/services/keys-locked-in-car/")],
    },
    "cape-coral": {
        "blurb": "Cape Coral’s canal communities, shopping centers, and long residential streets mean lockouts can leave you stranded far from a spare key — especially in afternoon heat.",
        "vehicle": "Cape Coral vehicle lockouts are common after errands, school runs, and waterfront stops. We provide mobile unlock help across the Cape.",
        "home": "Locked out of a Cape Coral house or apartment? Call with your street address and we will coordinate residential lockout assistance.",
        "nearby": ["fort-myers", "north-fort-myers", "fort-myers-beach"],
        "links": [("Cape Coral Car Lockouts", "/services/car-lockouts/"), ("Emergency Vehicle Lockouts", "/services/emergency-vehicle-lockout/"), ("Apartment Lockouts", "/services/apartment-lockouts/")],
    },
    "naples": {
        "blurb": "Naples combines coastal living with busy retail corridors and condo communities — lockouts happen at beach lots, grocery stops, and front doors alike.",
        "vehicle": "Whether you are locked out near Fifth Avenue, a beach parking area, or a residential street, Lockout Pro helps Naples drivers regain vehicle access.",
        "home": "Condo and home lockouts are frequent in Naples communities. Have your building or street address ready when you call.",
        "nearby": ["north-naples", "bonita-springs", "estero"],
        "links": [("Naples Home Lockouts", "/services/home-lockouts/"), ("Condo Lockouts", "/services/condo-lockouts/"), ("Car Lockouts", "/services/car-lockouts/")],
    },
    "bonita-springs": {
        "blurb": "Bonita Springs sits between Fort Myers and Naples with shopping plazas, residential communities, and beach access routes where lockouts are a real inconvenience.",
        "vehicle": "Locked out in a Bonita Springs parking lot or driveway? Mobile vehicle unlock help is a call away.",
        "home": "Residential lockouts in Bonita Springs neighborhoods and condo communities are part of our local coverage.",
        "nearby": ["estero", "naples", "fort-myers-beach"],
        "links": [("Vehicle Lockouts", "/services/car-lockouts/"), ("Home Lockouts", "/services/home-lockouts/"), ("Garage Lockouts", "/services/garage-lockouts/")],
    },
    "estero": {
        "blurb": "Estero’s mix of retail, residential, and FGCU-area traffic makes vehicle and home lockouts a frequent local need.",
        "vehicle": "From shopping centers to neighborhood streets, Estero drivers call Lockout Pro for car and SUV lockout help.",
        "home": "Apartment, condo, and house lockouts across Estero communities are covered — call with your address.",
        "nearby": ["bonita-springs", "san-carlos-park", "fort-myers"],
        "links": [("Car Lockouts", "/services/car-lockouts/"), ("Apartment Lockouts", "/services/apartment-lockouts/"), ("Emergency Lockouts", "/services/emergency-vehicle-lockout/")],
    },
    "north-naples": {
        "blurb": "North Naples blends busy commercial corridors with residential and condo living — lockouts happen on both sides of the day.",
        "vehicle": "North Naples vehicle lockouts are common after errands and appointments. We come to your location.",
        "home": "Condo and home lockout assistance is available across North Naples communities.",
        "nearby": ["naples", "bonita-springs", "estero"],
        "links": [("Condo Lockouts", "/services/condo-lockouts/"), ("Car Lockouts", "/services/car-lockouts/"), ("Home Lockouts", "/services/home-lockouts/")],
    },
    "fort-myers-beach": {
        "blurb": "Fort Myers Beach lockouts often happen after beach days, parking searches, and condo returns — when spare keys are nowhere nearby.",
        "vehicle": "Keys locked in the car near the beach or island parking? Call for mobile unlock help on Fort Myers Beach.",
        "home": "Condo and rental lockouts are a frequent beach-community call. Share the building name and unit when you can.",
        "nearby": ["fort-myers", "san-carlos-park", "bonita-springs"],
        "links": [("Trunk Lockouts", "/services/trunk-lockouts/"), ("Condo Lockouts", "/services/condo-lockouts/"), ("Emergency Lockouts", "/services/emergency-vehicle-lockout/")],
    },
    "lehigh-acres": {
        "blurb": "Lehigh Acres covers a wide residential footprint — distance from a spare key makes lockouts especially stressful.",
        "vehicle": "Car and truck lockouts across Lehigh Acres streets and driveways are part of our Lee County coverage.",
        "home": "House lockouts in Lehigh Acres happen day and night. Call with your address for residential unlock help.",
        "nearby": ["fort-myers", "san-carlos-park", "estero"],
        "links": [("Home Lockouts", "/services/home-lockouts/"), ("Car Lockouts", "/services/car-lockouts/"), ("Keys Locked In Car", "/services/keys-locked-in-car/")],
    },
    "san-carlos-park": {
        "blurb": "San Carlos Park sits along key routes between Fort Myers and Estero, with residential streets and commercial stops where lockouts occur.",
        "vehicle": "Locked out near US 41 or a neighborhood street in San Carlos Park? We provide mobile vehicle unlock help.",
        "home": "Residential lockout assistance is available for San Carlos Park homes and nearby communities.",
        "nearby": ["fort-myers", "estero", "fort-myers-beach"],
        "links": [("Car Lockouts", "/services/car-lockouts/"), ("Home Lockouts", "/services/home-lockouts/"), ("Emergency Residential Lockouts", "/services/emergency-residential-lockout/")],
    },
    "north-fort-myers": {
        "blurb": "North Fort Myers drivers and residents deal with lockouts across residential roads, shopping stops, and river-adjacent neighborhoods.",
        "vehicle": "Vehicle lockout help is available throughout North Fort Myers — call with your location and vehicle details.",
        "home": "Home and apartment lockouts in North Fort Myers are part of our local response coverage.",
        "nearby": ["fort-myers", "cape-coral", "lehigh-acres"],
        "links": [("Car Lockouts", "/services/car-lockouts/"), ("Apartment Lockouts", "/services/apartment-lockouts/"), ("Home Lockouts", "/services/home-lockouts/")],
    },
}

# Primary display order (homepage / nav lists):
# Estero, Bonita Springs, Naples, Fort Myers, San Carlos Park, Fort Myers Beach, Cape Coral
AREAS = [
    {"slug": "estero", "name": "Estero", "county": "Lee County", "primary": True},
    {"slug": "bonita-springs", "name": "Bonita Springs", "county": "Lee County", "primary": True},
    {"slug": "naples", "name": "Naples", "county": "Collier County", "primary": True},
    {"slug": "fort-myers", "name": "Fort Myers", "county": "Lee County", "primary": True},
    {"slug": "san-carlos-park", "name": "San Carlos Park", "county": "Lee County", "primary": True},
    {"slug": "fort-myers-beach", "name": "Fort Myers Beach", "county": "Lee County", "primary": True},
    {"slug": "cape-coral", "name": "Cape Coral", "county": "Lee County", "primary": True},
    {"slug": "north-naples", "name": "North Naples", "county": "Collier County"},
    {"slug": "lehigh-acres", "name": "Lehigh Acres", "county": "Lee County"},
    {"slug": "north-fort-myers", "name": "North Fort Myers", "county": "Lee County"},
]
PRIMARY_AREAS = [a for a in AREAS if a.get("primary")]

SERVICES = [
    # Automotive
    {
        "slug": "car-lockouts",
        "category": "automotive",
        "name": "Car Lockouts",
        "short": "Locked out of your car? We'll come to you and get you back inside.",
        "eyebrow": "AUTOMOTIVE",
        "h1": "Car Lockout Service in Southwest Florida",
        "meta_title": "Car Lockouts SWFL | Fast Vehicle Unlock | Lockout Pro",
        "meta_desc": "Locked out of your car in Fort Myers, Cape Coral, Naples or SWFL? Lockout Pro provides fast car lockout service. Call (239) 380-5240.",
        "intro": "Keys on the seat. Door locked. Heat climbing. Lockout Pro SWFL helps drivers across Southwest Florida get back into their cars quickly and carefully.",
        "body": [
            ("Help When You Need It", "Call with your location and vehicle details. We come to you — parking lots, driveways, workplaces, and roadside locations across SWFL."),
            ("What To Share When You Call", "Your exact location and vehicle year, make, and model help us arrive prepared. If a child or pet is inside, or the engine is running, tell us right away."),
            ("Professional Entry", "Modern vehicles aren't built for improvised tools. Professional lockout methods are designed to open the door carefully and get you moving again."),
        ],
        "faqs": [
            ("How fast can you unlock my car?", "Arrival time depends on your location and current calls. When you call, we give a realistic estimate for your area."),
            ("Will unlocking damage my door?", "We use professional entry methods intended to minimize risk. DIY tools are more likely to cause damage."),
            ("Do you help in Naples and Cape Coral?", "Yes — Fort Myers, Cape Coral, Naples, Estero, Bonita Springs, Lehigh Acres, and surrounding communities."),
            ("What if I'm locked out of my house too?", "We also help with home, apartment, condo, and garage lockouts. Call and we'll get you sorted."),
        ],
        "related": ["keys-locked-in-car", "truck-suv-lockouts", "trunk-lockouts", "emergency-vehicle-lockout"],
        "image": "/assets/images/hellcat.webp",
    },
    {
        "slug": "keys-locked-in-car",
        "category": "automotive",
        "name": "Keys Locked In Car",
        "short": "Keys locked in the car? Mobile unlock help across Southwest Florida.",
        "eyebrow": "AUTOMOTIVE",
        "h1": "Keys Locked In Car — Southwest Florida",
        "meta_title": "Keys Locked In Car SWFL | Unlock Help | Lockout Pro",
        "meta_desc": "Keys locked in your car in Fort Myers, Cape Coral, Naples or SWFL? Lockout Pro provides careful unlock help. Call (239) 380-5240.",
        "intro": "Keys on the seat. Doors locked. It happens to careful drivers every day across Southwest Florida. Lockout Pro SWFL helps you get back into your vehicle without turning a bad moment into vehicle damage.",
        "body": [
            ("Stay Calm And Stay Safe", "If a child or pet is inside — or the engine is running — say so immediately when you call. Move to a safe spot near the vehicle while you wait."),
            ("Share Vehicle Details", "Year, make, and model help us arrive prepared. Exact location (parking lot name, mile marker, address) speeds everything up."),
            ("Professional Entry Methods", "Modern vehicles are not designed for improvised tools. Professional lockout methods prioritize careful access so you can get moving again."),
            ("Common SWFL Situations", "Grocery runs, beach days, school drop-offs, and workplace lots are frequent lockout scenes from Fort Myers to Naples."),
        ],
        "faqs": [
            ("Can you unlock a car with keys inside?", "In many lockout situations, yes. Call with your vehicle details and location."),
            ("Will you damage my door or window?", "We use professional methods intended to minimize risk. DIY tools are more likely to cause damage."),
            ("What if keys are locked in the trunk?", "We also help with trunk lockouts — share the full situation when you call."),
            ("Do you help in Cape Coral and Naples?", "Yes — and surrounding Southwest Florida communities."),
        ],
        "related": ["car-lockouts", "trunk-lockouts", "emergency-vehicle-lockout", "home-lockouts"],
        "image": "/assets/images/hellcat.webp",
    },
    {
        "slug": "truck-suv-lockouts",
        "category": "automotive",
        "name": "Truck & SUV Lockouts",
        "short": "Locked out of your truck or SUV? Mobile unlock help across SWFL.",
        "eyebrow": "AUTOMOTIVE",
        "h1": "Truck & SUV Lockout Service",
        "meta_title": "Truck & SUV Lockouts SWFL | Lockout Pro",
        "meta_desc": "Locked out of a truck or SUV in Southwest Florida? Lockout Pro provides mobile unlock service. Call (239) 380-5240.",
        "intro": "Trucks and SUVs lock out just like cars — and Florida heat doesn't make waiting easier. Lockout Pro SWFL provides mobile unlock help for trucks and SUVs across Southwest Florida.",
        "body": [
            ("Built For Real-World Vehicles", "From daily-driver SUVs to work trucks, we help get you back inside when keys are locked in the cabin."),
            ("Job Sites And Parking Lots", "Whether you're at home, work, a store, or a job site, call with your location and vehicle details."),
            ("Clear Next Steps", "We'll confirm your location, give a realistic arrival window, and come to you."),
        ],
        "faqs": [
            ("Do you unlock pickup trucks?", "In many cases yes. Call with year, make, and model."),
            ("What about large SUVs?", "Yes — share your vehicle details when you call so we can prepare."),
            ("Are you available after hours?", "Yes. Emergency lockout help is available 24/7 across our service area."),
        ],
        "related": ["car-lockouts", "fleet-vehicle-lockouts", "emergency-vehicle-lockout"],
        "image": "/assets/images/hellcat.webp",
    },
    {
        "slug": "trunk-lockouts",
        "category": "automotive",
        "name": "Trunk Lockouts",
        "short": "Keys locked in the trunk? We'll help you regain access carefully.",
        "eyebrow": "AUTOMOTIVE",
        "h1": "Trunk Lockout Service",
        "meta_title": "Trunk Lockouts SWFL | Keys Locked In Trunk | Lockout Pro",
        "meta_desc": "Keys locked in the trunk in Fort Myers or SWFL? Lockout Pro provides professional trunk lockout help. Call (239) 380-5240.",
        "intro": "Keys in the trunk with no easy way back in — Lockout Pro SWFL helps with careful trunk lockout service across Southwest Florida.",
        "body": [
            ("The Right Approach For Your Vehicle", "Some vehicles allow cabin entry that restores trunk release. Others need a trunk-focused approach. We'll choose what fits your vehicle."),
            ("Protect Latches And Seals", "Forced entry can damage trunk hardware. Professional methods prioritize controlled access."),
            ("Common Situations", "Grocery runs, beach days, and busy parking lots are frequent trunk-lockout scenes across SWFL."),
        ],
        "faqs": [
            ("Can you open a trunk without keys?", "In many cases yes, using vehicle-appropriate techniques."),
            ("My keys are in the trunk and the car is locked — can you help?", "Yes. That's a common call for us."),
            ("Will you damage the trunk?", "Our goal is careful access whenever possible."),
        ],
        "related": ["car-lockouts", "emergency-vehicle-lockout", "truck-suv-lockouts"],
        "image": "/assets/images/hellcat.webp",
    },
    {
        "slug": "emergency-vehicle-lockout",
        "category": "automotive",
        "name": "Emergency Vehicle Lockouts",
        "short": "24/7 help when you're locked out of your vehicle.",
        "eyebrow": "24/7 EMERGENCY",
        "h1": "Emergency Vehicle Lockout Service",
        "meta_title": "Emergency Vehicle Lockouts SWFL | 24/7 | Lockout Pro",
        "meta_desc": "Emergency vehicle lockout help in Southwest Florida. Locked out day or night? Call Lockout Pro at (239) 380-5240.",
        "intro": "Lockouts don't wait for business hours. Lockout Pro SWFL provides emergency vehicle lockout help across Southwest Florida when you need assistance now.",
        "body": [
            ("Urgent Situations", "Call right away if someone is locked inside, the engine is running, you're in an unsafe area, or you're stranded in extreme heat."),
            ("Clear Communication", "When you call, we confirm your location, vehicle details, and a realistic arrival window."),
            ("Local Coverage", "Mobile response across Fort Myers, Cape Coral, Naples, Estero, Bonita Springs, and surrounding communities."),
        ],
        "faqs": [
            ("Are you available 24/7?", "Yes — emergency lockout help around the clock across our SWFL area."),
            ("What should I do while I wait?", "Stay near the vehicle in a safe place. Avoid forcing the door with household tools."),
            ("Do you also help with home lockouts?", "Yes. We help with vehicle and residential lockouts."),
        ],
        "related": ["car-lockouts", "trunk-lockouts", "emergency-residential-lockout"],
        "image": "/assets/images/hellcat.webp",
    },
    {
        "slug": "fleet-vehicle-lockouts",
        "category": "automotive",
        "name": "Fleet Vehicle Lockouts",
        "short": "Lockout help for work trucks, vans, and company vehicles.",
        "eyebrow": "AUTOMOTIVE",
        "h1": "Fleet Vehicle Lockout Service",
        "meta_title": "Fleet Vehicle Lockouts SWFL | Work Vehicle Unlock | Lockout Pro",
        "meta_desc": "Fleet vehicle locked out in SWFL? Lockout Pro helps with work truck, van, and company vehicle lockouts. Call (239) 380-5240.",
        "intro": "A locked work vehicle stops a job. Lockout Pro SWFL helps Southwest Florida businesses get fleet vehicles open again.",
        "body": [
            ("Practical Turnaround", "Share the vehicle details and location — we'll coordinate mobile lockout service across our coverage area."),
            ("Work Trucks And Vans", "Keys locked in cabins and job-site vehicles are common calls. We're ready to help."),
            ("One Number To Call", f"Reach us at {PHONE_DISPLAY} for fleet lockout assistance."),
        ],
        "faqs": [
            ("Do you help small business fleets?", "Yes — from a few vehicles to larger local fleets needing lockout help."),
            ("Can you unlock work trucks and vans?", "In many cases yes. Call with year, make, and model."),
            ("Do you come to job sites?", "Yes — mobile service to your location across SWFL."),
        ],
        "related": ["truck-suv-lockouts", "car-lockouts", "emergency-vehicle-lockout"],
        "image": "/assets/images/hellcat.webp",
    },
    # Residential
    {
        "slug": "home-lockouts",
        "category": "residential",
        "name": "Home Lockouts",
        "short": "Locked out of your house or commercial space? Fast, professional unlock help.",
        "eyebrow": "RESIDENTIAL",
        "h1": "Home & Commercial Lockout Service in Southwest Florida",
        "meta_title": "Home & Commercial Lockouts SWFL | Unlock Service | Lockout Pro",
        "meta_desc": "Locked out of your house or commercial space in Estero, Bonita Springs, Naples, Fort Myers or SWFL? Lockout Pro provides lockout service. Call (239) 380-5240.",
        "intro": "Locked out of your house, apartment, or commercial space? Lockout Pro SWFL provides professional residential and commercial lockout help across Southwest Florida — so you can get back inside without the stress spiral.",
        "body": [
            ("Back Inside Your Home", "Call with your address and a quick description of the door or lock situation. We'll come to you."),
            ("Houses Across SWFL", "From Fort Myers to Naples and nearby communities, we help homeowners who've been locked out."),
            ("Calm, Professional Help", "We'll walk you through next steps when you call and provide a realistic arrival estimate."),
        ],
        "faqs": [
            ("Can you unlock my front door?", "In many residential lockout situations, yes. Share details when you call."),
            ("Do I need to prove I live there?", "Be ready to confirm occupancy/ownership as needed for security."),
            ("Do you also unlock cars?", "Yes — we help with both home and vehicle lockouts."),
            ("Are you available at night?", "Yes. Emergency residential lockout help is available 24/7."),
        ],
        "related": ["apartment-lockouts", "condo-lockouts", "garage-lockouts", "emergency-residential-lockout"],
        "image": "/assets/images/resi.webp",
    },
    {
        "slug": "apartment-lockouts",
        "category": "residential",
        "name": "Apartment Lockouts",
        "short": "Locked out of your apartment? We'll help you get back in.",
        "eyebrow": "RESIDENTIAL",
        "h1": "Apartment Lockout Service",
        "meta_title": "Apartment Lockouts SWFL | Lockout Pro",
        "meta_desc": "Locked out of your apartment in Southwest Florida? Lockout Pro provides apartment lockout help. Call (239) 380-5240.",
        "intro": "Apartment lockouts happen — keys left inside, fob issues, or a door that closed behind you. Lockout Pro SWFL helps renters and residents get back inside.",
        "body": [
            ("Apartment Living, Real Lockouts", "Call with your building address and unit details so we can find you quickly."),
            ("Building Access Notes", "If a gate or lobby code is required, have that information ready when we arrive."),
            ("Friendly Local Help", "Clear communication and a calm process — especially when you're stuck outside with groceries, kids, or work bags."),
        ],
        "faqs": [
            ("Do you work in apartment complexes?", "Yes. Share the community name and address when you call."),
            ("What if my landlord needs to be notified?", "Follow your lease rules; we're here to help you regain access when appropriate."),
            ("Can you help if I'm locked out of my car in the lot too?", "Yes — vehicle lockouts are part of what we do."),
        ],
        "related": ["home-lockouts", "condo-lockouts", "emergency-residential-lockout"],
        "image": "/assets/images/apartment.jpg",
    },
    {
        "slug": "condo-lockouts",
        "category": "residential",
        "name": "Condo Lockouts",
        "short": "Locked out of your condo? Local unlock assistance across SWFL.",
        "eyebrow": "RESIDENTIAL",
        "h1": "Condo Lockout Service",
        "meta_title": "Condo Lockouts SWFL | Lockout Pro",
        "meta_desc": "Locked out of your condo in Southwest Florida? Lockout Pro provides condo lockout assistance. Call (239) 380-5240.",
        "intro": "Condo lockouts can leave you stuck at the door after a beach day, grocery run, or late night. Lockout Pro SWFL provides local condo lockout help.",
        "body": [
            ("Condo Communities Across SWFL", "From coastal buildings to inland communities, call with your address and we'll come to you."),
            ("Access Details Help", "Gate codes, building names, and parking instructions help us reach you faster."),
            ("Get Back To Your Evening", "Our goal is simple: help you get inside with clear communication along the way."),
        ],
        "faqs": [
            ("Do you service condo buildings in Naples and Fort Myers Beach?", "Yes — and surrounding Southwest Florida communities."),
            ("What information should I have ready?", "Address, unit number, and any gate/lobby access details."),
            ("Are weekend lockouts covered?", "Yes. We're available 24/7 for emergency lockout help."),
        ],
        "related": ["apartment-lockouts", "home-lockouts", "garage-lockouts"],
        "image": "/assets/images/home-premium.webp",
    },
    {
        "slug": "garage-lockouts",
        "category": "residential",
        "name": "Garage Lockouts",
        "short": "Locked out of your garage? We'll help restore access.",
        "eyebrow": "RESIDENTIAL",
        "h1": "Garage Lockout Service",
        "meta_title": "Garage Lockouts SWFL | Lockout Pro",
        "meta_desc": "Locked out of your garage in Southwest Florida? Lockout Pro provides garage lockout help. Call (239) 380-5240.",
        "intro": "Whether the garage door closed with keys inside or you're locked out of a side/garage entry door, Lockout Pro SWFL can help.",
        "body": [
            ("Garage Entry Situations", "Tell us whether you're dealing with a pedestrian door, overhead door scenario, or related access issue so we can prepare."),
            ("Home Access Matters", "Getting into the garage often means getting back into your day — tools, vehicles, and home access included."),
            ("Call For Guidance", "Not sure which service you need? Call and describe the situation. We'll point you in the right direction."),
        ],
        "faqs": [
            ("Can you unlock a garage side door?", "In many cases yes. Share details when you call."),
            ("What if my car is locked in the garage?", "Tell us the full situation — vehicle and garage access details help."),
            ("Do you help with house lockouts too?", "Yes. Home lockouts are a core service."),
        ],
        "related": ["home-lockouts", "car-lockouts", "emergency-residential-lockout"],
        "image": "/assets/images/home-premium.webp",
    },
    {
        "slug": "emergency-residential-lockout",
        "category": "residential",
        "name": "Emergency Residential Lockouts",
        "short": "24/7 home, apartment, and condo lockout assistance.",
        "eyebrow": "24/7 EMERGENCY",
        "h1": "Emergency Residential Lockout Service",
        "meta_title": "Emergency Home Lockouts SWFL | 24/7 | Lockout Pro",
        "meta_desc": "Emergency residential lockout help in Southwest Florida. Locked out of your home, apartment, or condo? Call (239) 380-5240.",
        "intro": "Being locked out at night — or with kids, pets, or groceries in tow — is stressful. Lockout Pro SWFL provides emergency residential lockout help across Southwest Florida.",
        "body": [
            ("When You Need Help Now", "Call with your address and a brief description of the lockout. We'll provide a realistic arrival estimate."),
            ("Homes, Apartments, And Condos", "Emergency residential lockout assistance for the places people live across SWFL."),
            ("Reassuring Process", "Clear communication, professional service, and a focus on getting you back inside."),
        ],
        "faqs": [
            ("Are residential lockouts available 24/7?", "Yes."),
            ("What areas do you cover?", "Fort Myers, Cape Coral, Naples, Estero, Bonita Springs, and surrounding Southwest Florida communities."),
            ("Can you also help if my keys are locked in the car?", "Yes — vehicle lockouts are part of what we do."),
        ],
        "related": ["home-lockouts", "apartment-lockouts", "emergency-vehicle-lockout"],
        "image": "/assets/images/home-premium.webp",
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}
AUTO_SERVICES = [s for s in SERVICES if s["category"] == "automotive"]
HOME_SERVICES = [s for s in SERVICES if s["category"] == "residential"]

# Soft redirects for old URLs — helpful, not restrictive
SERVICE_REDIRECTS = {
    "lost-car-keys": (f"{AGL}/services/car-key-replacement/", "Looking for car key help? A Good Locksmith can assist with key replacement. If you're locked out with keys inside, call Lockout Pro."),
    "car-key-replacement": (f"{AGL}/services/car-key-replacement/", "For car key replacement, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "key-fob-programming": (f"{AGL}/services/key-programming/", "For key fob programming, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "smart-keys": (f"{AGL}/services/automotive-locksmith/", "For smart key help, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "push-to-start-keys": (f"{AGL}/services/automotive-locksmith/", "For push-to-start key help, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "broken-car-key-extraction": (f"{AGL}/services/automotive-locksmith/", "For broken key extraction, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "ignition-repair": (f"{AGL}/services/automotive-locksmith/", "For ignition assistance, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "duplicate-car-keys": (f"{AGL}/services/car-key-replacement/", "For spare keys, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "motorcycle-keys": (f"{AGL}/services/automotive-locksmith/", "For motorcycle key help, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "emergency-automotive-locksmith": ("/services/emergency-vehicle-lockout/", "This page has moved to Emergency Vehicle Lockouts."),
    "fleet-vehicle-locksmith": ("/services/fleet-vehicle-lockouts/", "This page has moved to Fleet Vehicle Lockouts."),
    "commercial-vehicle-lockout": ("/services/truck-suv-lockouts/", "Looking for commercial or truck lockout help? See Truck & SUV Lockouts."),
}

RESOURCES = [
    {
        "slug": "locked-out-of-your-car",
        "title": "Locked Out Of Your Car? Here's What To Do",
        "eyebrow": "VEHICLE GUIDE",
        "meta_desc": "Locked your keys in the car in SWFL? Stay safe, avoid damage, and get help fast.",
        "minutes": 5,
        "image": "/assets/images/hellcat.webp",
        "intro": "A car lockout rarely happens at a convenient time. Here's what to do next — stay safe, avoid damage, and get help.",
        "sections": [
            ("1. Check Safety First", "If a child or pet is inside, call for help immediately. Move to a safe place near the vehicle."),
            ("2. Confirm It's Locked", "Try every door and check for a spare before forcing anything."),
            ("3. Avoid DIY Entry Tools", "Improvised tools commonly damage seals, paint, wiring, or linkages."),
            ("4. Call For Lockout Help", "Share your location and vehicle year/make/model. Lockout Pro SWFL is ready to help across Southwest Florida."),
            ("5. After You're Back In", "Consider a spare-key plan so the next lockout is less likely."),
        ],
        "faqs": [
            ("Can you unlock my car without damaging it?", "In most lockout situations, professional methods aim for careful entry."),
            ("Do you also unlock homes?", "Yes — home, apartment, condo, and garage lockouts too."),
        ],
    },
    {
        "slug": "locked-out-of-your-house",
        "title": "Locked Out Of Your House? Here's What To Do",
        "eyebrow": "HOME GUIDE",
        "meta_desc": "Locked out of your house in SWFL? Practical next steps and when to call for lockout help.",
        "minutes": 4,
        "image": "/assets/images/home-premium.webp",
        "intro": "Being locked out of your house is stressful — especially with kids, pets, or Florida heat. Here's a calm plan.",
        "sections": [
            ("1. Check Other Entries", "Try side doors, garage access, and whether anyone else has a key."),
            ("2. Stay Safe", "If it's dark or you're in an unsafe spot, move to a well-lit area and call for help."),
            ("3. Avoid Forcing The Door", "Prying and improvised tools can damage doors, frames, and locks."),
            ("4. Call Lockout Pro", "Share your address and a quick description of the lockout. We'll give a realistic arrival estimate."),
            ("5. After You're Inside", "If keys are frequently misplaced, consider a spare plan with someone you trust."),
        ],
        "faqs": [
            ("Can you unlock apartment and condo doors too?", "Yes — residential lockouts include homes, apartments, and condos."),
            ("Are you available at night?", "Yes. Emergency residential lockout help is available 24/7."),
        ],
    },
    {
        "slug": "prevent-locking-keys-in-your-car",
        "title": "How To Prevent Locking Keys In Your Car",
        "eyebrow": "PREVENTION",
        "meta_desc": "Simple habits to reduce car lockouts for Southwest Florida drivers.",
        "minutes": 3,
        "image": "/assets/images/hellcat.webp",
        "intro": "Most car lockouts are preventable. A few habits go a long way.",
        "sections": [
            ("Keep Keys In A Fixed Place", "Same pocket or bag pocket every time."),
            ("Learn Auto-Lock Behavior", "Know whether your vehicle locks automatically."),
            ("Have A Spare Strategy", "A spare kept separately is the simplest prevention."),
            ("Pause Before Walking Away", "Especially with soft-close doors and busy hands."),
        ],
        "faqs": [
            ("What's the best prevention tip?", "A working spare stored separately from your daily key."),
        ],
    },
    {
        "slug": "how-much-does-a-car-lockout-cost",
        "title": "How Much Does A Car Lockout Cost?",
        "eyebrow": "PRICING",
        "meta_desc": "What affects car lockout pricing in Southwest Florida.",
        "minutes": 4,
        "image": "/assets/images/automotive-work.jpg",
        "intro": "Lockout pricing isn't one flat number — vehicle type, location, timing, and complexity all matter.",
        "sections": [
            ("Vehicle Details Matter", "Year, make, and model help with preparation and clearer estimates."),
            ("Location And Timing", "After-hours and farther locations can affect response."),
            ("Complexity", "A straightforward cabin lockout can differ from certain trunk situations."),
            ("Ask For Clarity", "Provide accurate details and ask for a clear estimate when you call."),
        ],
        "faqs": [
            ("Why can't I get an exact price by text?", "Vehicles and situations vary. Details help."),
        ],
    },
    {
        "slug": "locked-out-engine-running",
        "title": "Locked Out With The Engine Running?",
        "eyebrow": "URGENT",
        "meta_desc": "Locked out of a running car in SWFL? What to do next.",
        "minutes": 3,
        "image": "/assets/images/hellcat.webp",
        "intro": "A running vehicle with keys inside raises the stakes. Stay calm and call for help.",
        "sections": [
            ("Call Immediately", "Tell us the engine is running and share your location plus vehicle details."),
            ("Stay With The Vehicle If Safe", "Don't leave a running vehicle unattended if you can safely remain nearby."),
            ("Kids Or Pets Inside", "Say so immediately when you call."),
            ("Avoid Breaking A Window First", "Professional entry is usually the better first call."),
        ],
        "faqs": [
            ("Is this more urgent?", "Yes — especially with occupants inside or extreme heat."),
        ],
    },
    {
        "slug": "how-to-get-back-into-car-without-keys",
        "title": "How Do I Get Back Into My Car Without Keys?",
        "eyebrow": "VEHICLE GUIDE",
        "meta_desc": "Locked out without keys in SWFL? Safer next steps than forcing a door — and when to call for unlock help.",
        "minutes": 4,
        "image": "/assets/images/hellcat.webp",
        "intro": "Getting back into a locked car without keys is a common search — and a moment when DIY mistakes get expensive. Here is a calm, practical approach.",
        "sections": [
            ("Confirm The Doors Are Actually Locked", "Try every door and hatch before assuming you need forced entry."),
            ("Check For A Spare", "Home spare, partner, or lockbox — a spare is still the simplest fix."),
            ("Skip Improvised Tools", "Wedges, coat hangers, and YouTube hacks commonly damage seals, paint, and wiring."),
            ("Call A Local Lockout Pro", "Share your location and vehicle year/make/model. Lockout Pro SWFL provides mobile unlock help across Southwest Florida."),
            ("Related Help", "If keys are in the trunk, see our trunk lockout resources. If you are locked out of your house too, we can help with residential lockouts."),
        ],
        "faqs": [
            ("Can a locksmith unlock a car without damaging it?", "Professional methods are designed for careful entry. Results depend on the vehicle and situation."),
            ("Who do I call if I lock my keys in my car?", "In Southwest Florida, call Lockout Pro at (239) 380-5240."),
        ],
    },
    {
        "slug": "keys-locked-in-trunk-what-to-do",
        "title": "Keys Locked In The Trunk? What To Do Next",
        "eyebrow": "VEHICLE GUIDE",
        "meta_desc": "Keys locked in the trunk in Southwest Florida? Practical next steps and professional unlock options.",
        "minutes": 4,
        "image": "/assets/images/hellcat.webp",
        "intro": "Trunk lockouts are frustrating — especially after grocery runs or beach days. Here is what to do before the situation gets worse.",
        "sections": [
            ("Do Not Force The Trunk", "Prying can damage latches, seals, and paint quickly."),
            ("Check Cabin Access Options", "On some vehicles, unlocking the cabin restores trunk release. On others, a trunk-focused approach is needed."),
            ("Share Exact Details When You Call", "Tell us whether the cabin is also locked and share year, make, and model."),
            ("Local SWFL Help", "Lockout Pro provides trunk lockout assistance across Fort Myers, Cape Coral, Naples, and nearby communities."),
        ],
        "faqs": [
            ("Can you open a trunk without keys?", "In many cases yes, using vehicle-appropriate techniques."),
            ("Is a trunk lockout different from a cabin lockout?", "Sometimes. Vehicle design determines the best approach."),
        ],
    },
    {
        "slug": "can-locksmith-unlock-car-without-damage",
        "title": "Can A Locksmith Unlock A Car Without Damaging It?",
        "eyebrow": "VEHICLE FAQ",
        "meta_desc": "Learn how professional car lockout methods prioritize careful entry versus risky DIY tools.",
        "minutes": 3,
        "image": "/assets/images/hellcat.webp",
        "intro": "Damage is the biggest fear during a car lockout. Professional unlock methods exist specifically to reduce that risk.",
        "sections": [
            ("Why DIY Tools Are Risky", "Improvised wedges and hooks often stress weather seals, paint edges, and interior linkages."),
            ("What Professionals Aim For", "Controlled entry methods matched to the vehicle design."),
            ("What Helps Most", "Accurate vehicle details and a clear description of the lockout."),
            ("When To Call Immediately", "Child or pet inside, engine running, extreme heat, or an unsafe location."),
        ],
        "faqs": [
            ("Is damage ever possible?", "Any entry method carries some risk. Professional service is intended to minimize it versus DIY."),
            ("Should I break a window?", "Usually not as a first option — call for professional help first when it is safe to wait."),
        ],
    },
    {
        "slug": "does-roadside-assistance-cover-car-lockout",
        "title": "Does Roadside Assistance Cover A Car Lockout?",
        "eyebrow": "PLANNING",
        "meta_desc": "Roadside assistance and car lockouts — what to check, and how Lockout Pro can help in SWFL.",
        "minutes": 3,
        "image": "/assets/images/hellcat.webp",
        "intro": "Some roadside plans include lockout help. Coverage varies — and wait times can be long when you need help now.",
        "sections": [
            ("Check Your Plan Details", "Coverage, limits, and response expectations differ by provider."),
            ("Time Matters In Florida Heat", "Waiting can be uncomfortable or unsafe — especially with kids, pets, or a running vehicle."),
            ("Local Lockout Option", "Lockout Pro SWFL provides direct lockout help across Southwest Florida when you need a local response."),
            ("Have Details Ready", "Membership info (if using roadside) plus vehicle year/make/model and exact location."),
        ],
        "faqs": [
            ("Can I call Lockout Pro even if I have roadside assistance?", "Yes. Many people call a local lockout service for faster or clearer help."),
        ],
    },
    {
        "slug": "how-long-does-locksmith-take-unlock-car",
        "title": "How Long Does It Take A Locksmith To Unlock A Car?",
        "eyebrow": "TIMING",
        "meta_desc": "What affects arrival and unlock timing for car lockouts in Southwest Florida.",
        "minutes": 3,
        "image": "/assets/images/hellcat.webp",
        "intro": "Two clocks matter in a lockout: arrival time and unlock time. Both depend on location, demand, and vehicle details.",
        "sections": [
            ("Arrival Depends On Location", "Fort Myers, Cape Coral, Naples, and nearby communities have different travel patterns and call volume."),
            ("Ask For A Realistic Estimate", "When you call, we provide an estimate based on your area and current calls."),
            ("Unlock Time Varies By Vehicle", "Once on scene, many lockouts are completed relatively quickly — complexity still varies."),
            ("Help Us Help You Faster", "Exact address/pin, vehicle details, and urgency notes (engine running, occupants) speed the process."),
        ],
        "faqs": [
            ("Can you give an exact ETA online?", "Not without your location and current call status — calling is fastest."),
        ],
    },
    {
        "slug": "locked-out-of-apartment-what-to-do",
        "title": "Locked Out Of Your Apartment? What To Do",
        "eyebrow": "HOME GUIDE",
        "meta_desc": "Locked out of an apartment in SWFL? Practical next steps and when to call for lockout help.",
        "minutes": 4,
        "image": "/assets/images/home-premium.webp",
        "intro": "Apartment lockouts are stressful — especially with groceries, kids, or a late shift. Here is a simple plan.",
        "sections": [
            ("Check Building Options", "Roommate, neighbor with a spare, or after-hours management policy if available."),
            ("Avoid Forcing The Door", "Damaged frames and locks create bigger problems than the lockout itself."),
            ("Have Access Details Ready", "Community name, gate code, building, and unit help responders find you quickly."),
            ("Call For Residential Lockout Help", "Lockout Pro SWFL helps with apartment lockouts across Southwest Florida — call (239) 380-5240."),
        ],
        "faqs": [
            ("Can a locksmith unlock an apartment?", "In many residential lockout situations, yes. Share details when you call."),
            ("Do you also unlock cars in the parking lot?", "Yes — vehicle lockouts are part of what we do."),
        ],
    },
    {
        "slug": "can-locksmith-unlock-house",
        "title": "Can A Locksmith Unlock A House?",
        "eyebrow": "HOME FAQ",
        "meta_desc": "Yes — residential lockout help is available across Southwest Florida for houses and more.",
        "minutes": 3,
        "image": "/assets/images/home-premium.webp",
        "intro": "If you are locked out of your house, professional residential lockout help is often the safest next step.",
        "sections": [
            ("House Lockouts Are Common", "Keys left inside, doors that latch behind you, and misplaced spares happen every day."),
            ("What To Share When You Call", "Address, which door is locked, and any urgency details."),
            ("Homes, Apartments, Condos, Garages", "Lockout Pro helps across residential lockout situations in Southwest Florida."),
            ("After You Are Back Inside", "Consider a spare-key plan with someone you trust."),
        ],
        "faqs": [
            ("Do I need to prove I live there?", "Be ready to confirm occupancy or ownership as needed for security."),
            ("Are house unlocks available at night?", "Yes — emergency residential lockout help is available 24/7."),
        ],
    },
]

RESOURCE_REDIRECTS = {
    "lost-car-keys-guide": ("/resources/locked-out-of-your-car/", "Looking for lockout help? Start with our car lockout guide."),
    "how-much-does-a-car-locksmith-cost": ("/resources/how-much-does-a-car-lockout-cost/", "Updated guide focused on lockout pricing."),
    "key-fob-stopped-working": (AGL + "/", "For key fob help, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "can-a-locksmith-replace-push-to-start-keys": (AGL + "/", "For push-to-start keys, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "signs-ignition-cylinder-failing": (AGL + "/", "For ignition concerns, visit A Good Locksmith. Locked out? Call Lockout Pro."),
    "spare-car-keys-every-driver": (f"{AGL}/services/car-key-replacement/", "For spare keys, visit A Good Locksmith. Locked out? Call Lockout Pro."),
}


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def header(active: str = "") -> str:
    def cls(name):
        return ' class="is-active"' if active == name else ""

    return f'''<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="/" aria-label="{BRAND} home">
      <img src="/LOGO.png" alt="{BRAND}" class="brand-logo" width="44" height="44">
      <span class="brand-name"><span class="brand-lockout">LOCKOUT</span> <span class="brand-pro">PRO</span> <span class="brand-swfl">SWFL</span></span>
    </a>
    <nav class="main-nav" aria-label="Primary">
      <ul class="nav-list">
        <li><a href="/"{cls("home")}>Home</a></li>
        <li><a href="/services/"{cls("services")}>Services</a></li>
        <li><a href="/locations/"{cls("locations")}>Areas</a></li>
        <li><a href="/resources/"{cls("resources")}>Resources</a></li>
        <li><a href="/#contact"{cls("contact")}>Contact</a></li>
      </ul>
    </nav>
    <a class="header-phone" href="tel:{PHONE_TEL}">
      <span class="header-phone-label">24/7</span>
      <span class="header-phone-num">{PHONE_DISPLAY}</span>
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div id="mobile-nav" class="mobile-nav" hidden>
    <a href="/">Home</a>
    <a href="/services/">Services</a>
    <a href="/locations/">Service Areas</a>
    <a href="/resources/">Resources</a>
    <a href="/#faq">FAQ</a>
    <a href="/#contact">Contact</a>
    <a class="mobile-call" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  </div>
</header>'''


def footer() -> str:
    auto_links = "\n".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in AUTO_SERVICES[:4])
    home_links = "\n".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in HOME_SERVICES[:4])
    area_links = "\n".join(f'<li><a href="/locations/{a["slug"]}/">{esc(a["name"])}</a></li>' for a in PRIMARY_AREAS[:4])
    return f'''<footer class="site-footer" id="contact">
  <div class="container footer-grid">
    <div class="footer-brand">
      <a class="brand footer-brand-link" href="/">
        <img src="/LOGO.png" alt="{BRAND}" width="44" height="44">
        <span class="brand-name"><span class="brand-lockout">LOCKOUT</span> <span class="brand-pro">PRO</span> <span class="brand-swfl">SWFL</span></span>
      </a>
      <a class="footer-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <p class="footer-hours">24/7 · Southwest Florida</p>
    </div>
    <div>
      <h3>Vehicle</h3>
      <ul>{auto_links}</ul>
    </div>
    <div>
      <h3>Home</h3>
      <ul>{home_links}</ul>
    </div>
    <div>
      <h3>Areas</h3>
      <ul>{area_links}
        <li><a href="/locations/">All Areas →</a></li>
      </ul>
      <a class="footer-outlink" href="{AGL}" rel="noopener noreferrer" target="_blank">A Good Locksmith →</a>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <p>© {date.today().year} {BRAND}</p>
      <p>Southwest Florida</p>
    </div>
  </div>
</footer>
<a href="tel:{PHONE_TEL}" class="sticky-call" aria-label="Call {BRAND} now">
  <span class="sticky-call-kicker">Locked Out?</span>
  <span class="sticky-call-num">CALL {PHONE_DISPLAY}</span>
</a>
<script src="/script.js" defer></script>'''


def head(title, description, canonical, og_image=f"{DOMAIN}/assets/images/hero-desktop.webp", schemas=None, article=False):
    schema_html = ""
    if schemas:
        for schema in schemas:
            schema_html += '\n<script type="application/ld+json">\n' + json.dumps(schema, indent=2) + "\n</script>"
    og_type = "article" if article else "website"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="author" content="{BRAND}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#FF7A00">
<meta name="format-detection" content="telephone=yes">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="{BRAND}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{og_image}">
<link rel="icon" href="/LOGO.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
{schema_html}
</head>'''


def breadcrumbs(items):
    lis, schema_items = [], []
    for i, (name, href) in enumerate(items, 1):
        if href:
            lis.append(f'<li><a href="{href}">{esc(name)}</a></li>')
            schema_items.append({"@type": "ListItem", "position": i, "name": name, "item": DOMAIN + href if href.startswith("/") else href})
        else:
            lis.append(f'<li aria-current="page"><span>{esc(name)}</span></li>')
            schema_items.append({"@type": "ListItem", "position": i, "name": name})
    nav = f'''<div class="container breadcrumb-wrap"><nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav></div>'''
    return nav, {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": schema_items}


def sidebar(current=None):
    auto = "\n".join(
        '<li><a href="/services/{s}/"{c}>{n}</a></li>'.format(
            s=x["slug"], c=' class="current"' if current == x["slug"] else "", n=esc(x["name"])
        ) for x in AUTO_SERVICES
    )
    home = "\n".join(
        '<li><a href="/services/{s}/"{c}>{n}</a></li>'.format(
            s=x["slug"], c=' class="current"' if current == x["slug"] else "", n=esc(x["name"])
        ) for x in HOME_SERVICES
    )
    return f'''<aside class="page-sidebar">
  <div class="sidebar-card sidebar-cta">
    <p class="sidebar-kicker">Locked Out?</p>
    <a class="sidebar-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
    <a class="btn btn-primary btn-block" href="tel:{PHONE_TEL}">Call Now</a>
    <p class="sidebar-note">24/7 lockout help across SWFL</p>
  </div>
  <div class="sidebar-card">
    <h3>Vehicle</h3>
    <ul class="sidebar-links">{auto}</ul>
  </div>
  <div class="sidebar-card">
    <h3>Home</h3>
    <ul class="sidebar-links">{home}</ul>
  </div>
</aside>'''


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }


def faq_html(faqs):
    return "\n".join(
        f'''<details class="faq-item"><summary>{esc(q)}</summary><div class="faq-answer"><p>{esc(a)}</p></div></details>'''
        for q, a in faqs
    )


def org_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Locksmith",
        "name": BRAND,
        "url": DOMAIN + "/",
        "logo": DOMAIN + "/LOGO.png",
        "image": DOMAIN + "/assets/images/hero.webp",
        "telephone": PHONE_SCHEMA,
        "priceRange": "$$",
        "description": "24/7 lockout help across Southwest Florida — vehicle lockouts and home lockouts for cars, trucks, SUVs, houses, apartments, condos, and garages.",
        "areaServed": [a["name"] for a in AREAS] + ["Southwest Florida"],
        "serviceType": [s["name"] for s in SERVICES],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59",
        },
    }


def redirect_page(title, message, target, canonical):
    external = target.startswith("http")
    return f'''{head(title, message, canonical)}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("services")}
<section class="page-hero" id="main">
  <div class="page-hero-media" style="background-image:url('/assets/images/hero.webp')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">LOCKOUT PRO SWFL</p>
    <h1>{esc(title)}</h1>
    <p class="page-hero-lead">{esc(message)}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      <a class="btn btn-ghost" href="{target}"{" rel=\"noopener noreferrer\" target=\"_blank\"" if external else ""}>Continue →</a>
    </div>
  </div>
</section>
<meta http-equiv="refresh" content="8;url={target}">
<section class="section"><div class="container" style="max-width:720px"><div class="content-block">
<p>Locked out of your vehicle or home? Call <a href="tel:{PHONE_TEL}"><strong>{PHONE_DISPLAY}</strong></a>.</p>
<p style="margin-top:1rem"><a class="btn btn-primary" href="{target}"{" rel=\"noopener noreferrer\" target=\"_blank\"" if external else ""}>Go to the right page</a></p>
</div></div></section>
{footer()}
</body></html>'''


def build_service_pages():
    def cards(items):
        return "\n".join(
            f'''<a class="service-tile" href="/services/{s["slug"]}/">
  <span class="service-tile-eyebrow">{esc(s["eyebrow"])}</span>
  <h2>{esc(s["name"])}</h2>
  <p>{esc(s["short"])}</p>
  <span class="service-tile-link">Learn more →</span>
</a>''' for s in items
        )

    crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Services", None)])
    html = f'''{head(
        f"Lockout Services | Vehicle & Home | {BRAND}",
        "Lockout Pro SWFL lockout services for cars, trucks, SUVs, homes, apartments, condos, and garages across Southwest Florida.",
        f"{DOMAIN}/services/",
        schemas=[org_schema(), crumb_schema],
    )}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("services")}
<section class="page-hero" id="main">
  <div class="page-hero-media" style="background-image:url('/assets/images/hero.webp')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">LOCKOUT SERVICES</p>
    <h1>Vehicle &amp; Home Lockouts</h1>
    <p class="page-hero-lead">Fast local help when you're locked out across Southwest Florida.</p>
    <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  </div>
</section>
{crumb_nav}
<section class="section">
  <div class="container">
    <div class="section-head"><p class="eyebrow">AUTOMOTIVE</p><h2>Vehicle Lockouts</h2></div>
    <div class="service-tile-grid">{cards(AUTO_SERVICES)}</div>
    <div class="section-head" style="margin-top:3rem"><p class="eyebrow">RESIDENTIAL</p><h2>Home Lockouts</h2></div>
    <div class="service-tile-grid">{cards(HOME_SERVICES)}</div>
  </div>
</section>
<section class="roadside-cta">
  <div class="container roadside-cta-inner">
    <div><p class="eyebrow">NEED HELP NOW?</p><h2>Locked Out? We're On The Way.</h2></div>
    <a class="btn btn-primary btn-xl" href="tel:{PHONE_TEL}">CALL NOW {PHONE_DISPLAY}</a>
  </div>
</section>
{footer()}
</body></html>'''
    write(ROOT / "services" / "index.html", html)

    for s in SERVICES:
        related = "".join(
            f'<li><a href="/services/{slug}/">{esc(SERVICE_BY_SLUG[slug]["name"])}</a></li>'
            for slug in s["related"] if slug in SERVICE_BY_SLUG
        )
        body = "".join(f'<section class="content-block"><h2>{esc(h)}</h2><p>{esc(p)}</p></section>' for h, p in s["body"])
        areas = ", ".join(f'<a href="/locations/{a["slug"]}/">{esc(a["name"])}</a>' for a in PRIMARY_AREAS[:4])
        crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Services", "/services/"), (s["name"], None)])
        service_schema = {
            "@context": "https://schema.org", "@type": "Service",
            "name": s["name"], "serviceType": s["name"], "description": s["meta_desc"],
            "url": f"{DOMAIN}/services/{s['slug']}/",
            "provider": {"@type": "Locksmith", "name": BRAND, "telephone": PHONE_SCHEMA, "url": DOMAIN + "/"},
            "areaServed": [a["name"] for a in AREAS],
        }
        html = f'''{head(s["meta_title"], s["meta_desc"], f"{DOMAIN}/services/{s['slug']}/", DOMAIN + s["image"], [service_schema, crumb_schema, faq_schema(s["faqs"])])}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("services")}
<section class="page-hero" id="main">
  <div class="page-hero-media" style="background-image:url('{s["image"]}')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">{esc(s["eyebrow"])}</p>
    <h1>{esc(s["h1"])}</h1>
    <p class="page-hero-lead">{esc(s["short"])}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      <a class="btn btn-ghost" href="/services/">All Services</a>
    </div>
  </div>
</section>
{crumb_nav}
<section class="section page-layout">
  <div class="container page-layout-grid">
    <div class="page-main">
      <div class="content-block intro-block">
        <p>{esc(s["intro"])}</p>
        <p>Serving {areas}, and nearby communities. Call <strong>{PHONE_DISPLAY}</strong>.</p>
      </div>
      {body}
      <section class="content-block"><h2>Service Areas</h2><p>Available across Southwest Florida, including {areas}.</p></section>
      <section class="content-block"><h2>Related Services</h2><ul class="text-list">{related}</ul></section>
      <section class="content-block"><h2>Guides</h2><ul class="text-list">
        <li><a href="/resources/locked-out-of-your-car/">Locked out of your car?</a></li>
        <li><a href="/resources/locked-out-of-your-house/">Locked out of your house?</a></li>
        <li><a href="/resources/how-much-does-a-car-lockout-cost/">How much does a car lockout cost?</a></li>
      </ul></section>
      <section class="content-block"><h2>FAQ</h2><div class="faq-list">{faq_html(s["faqs"])}</div></section>
    </div>
    {sidebar(s["slug"])}
  </div>
</section>
<section class="roadside-cta">
  <div class="container roadside-cta-inner">
    <div><p class="eyebrow">READY FOR HELP?</p><h2>Call Lockout Pro SWFL</h2></div>
    <a class="btn btn-primary btn-xl" href="tel:{PHONE_TEL}">CALL {PHONE_DISPLAY}</a>
  </div>
</section>
{footer()}
</body></html>'''
        write(ROOT / "services" / s["slug"] / "index.html", html)

    for old, (target, msg) in SERVICE_REDIRECTS.items():
        write(ROOT / "services" / old / "index.html", redirect_page(old.replace("-", " ").title(), msg, target, f"{DOMAIN}/services/{old}/"))


def build_location_pages():
    cards = "\n".join(
        f'''<a class="area-tile" href="/locations/{a["slug"]}/">
  <span class="area-tile-county">{esc(a["county"])}</span>
  <h2>{esc(a["name"])}</h2>
  <p>Vehicle and home lockout help in {esc(a["name"])}.</p>
  <span class="service-tile-link">View area →</span>
</a>''' for a in AREAS
    )
    crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Service Areas", None)])
    write(ROOT / "locations" / "index.html", f'''{head(
        f"Service Areas | Lockouts Across SWFL | {BRAND}",
        "Lockout Pro SWFL serves Fort Myers, Cape Coral, Naples, Bonita Springs, Estero and more with vehicle and home lockout help.",
        f"{DOMAIN}/locations/", schemas=[org_schema(), crumb_schema],
    )}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("locations")}
<section class="page-hero" id="main">
  <div class="page-hero-media" style="background-image:url('/assets/images/map.webp')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">SOUTHWEST FLORIDA</p>
    <h1>Areas We Serve</h1>
    <p class="page-hero-lead">Local lockout help across Lee and Collier County communities.</p>
    <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  </div>
</section>
{crumb_nav}
<section class="section"><div class="container area-tile-grid">{cards}</div></section>
{footer()}
</body></html>''')

    for a in AREAS:
        detail = AREA_DETAILS.get(a["slug"], {})
        auto = "".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])} in {esc(a["name"])}</a></li>' for s in AUTO_SERVICES[:5])
        home = "".join(f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])} in {esc(a["name"])}</a></li>' for s in HOME_SERVICES[:4])
        useful = "".join(f'<li><a href="{href}">{esc(label)}</a></li>' for label, href in detail.get("links", []))
        near_slugs = detail.get("nearby")
        if near_slugs:
            others = "".join(f'<li><a href="/locations/{o["slug"]}/">{esc(o["name"])}</a></li>' for o in AREAS if o["slug"] in near_slugs)
        else:
            others = "".join(f'<li><a href="/locations/{o["slug"]}/">{esc(o["name"])}</a></li>' for o in AREAS if o["slug"] != a["slug"])
        crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Service Areas", "/locations/"), (a["name"], None)])
        faqs = [
            (f"Do you unlock cars in {a['name']}?", f"Yes. We provide vehicle lockout help throughout {a['name']} and nearby {a['county']} communities."),
            (f"Can you help if I'm locked out of my house in {a['name']}?", f"Yes — home, apartment, condo, and garage lockouts in {a['name']}."),
            ("How fast can you arrive?", "Arrival time depends on your exact location and current calls. We'll give a realistic estimate when you call."),
            ("Are you available 24/7?", "Yes."),
        ]
        local = {
            "@context": "https://schema.org", "@type": "Locksmith",
            "name": f"{BRAND} — {a['name']}", "url": f"{DOMAIN}/locations/{a['slug']}/",
            "telephone": PHONE_SCHEMA, "areaServed": a["name"],
            "description": f"Vehicle and home lockout help in {a['name']}, {a['county']}, Florida.",
            "parentOrganization": {"@type": "Locksmith", "name": BRAND, "url": DOMAIN + "/"},
        }
        write(ROOT / "locations" / a["slug"] / "index.html", f'''{head(
            f"Lockouts in {a['name']} FL | Car & Home | {BRAND}",
            f"Locked out in {a['name']}? Lockout Pro SWFL helps with car lockouts and home lockouts. Call {PHONE_DISPLAY}.",
            f"{DOMAIN}/locations/{a['slug']}/", schemas=[local, crumb_schema, faq_schema(faqs)],
        )}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("locations")}
<section class="page-hero" id="main">
  <div class="page-hero-media" style="background-image:url('/assets/images/hero.webp')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">{esc(a["county"]).upper()}</p>
    <h1>Lockouts in {esc(a["name"])}</h1>
    <p class="page-hero-lead">Vehicle and home lockout help for {esc(a["name"])} residents and drivers.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      <a class="btn btn-ghost" href="/services/">View Services</a>
    </div>
  </div>
</section>
{crumb_nav}
<section class="section page-layout">
  <div class="container page-layout-grid">
    <div class="page-main">
      <div class="content-block intro-block">
        <p>Locked out in <strong>{esc(a["name"])}</strong>? Lockout Pro SWFL helps with vehicle and home lockouts across {esc(a["county"])}.</p>
        <p>{esc(detail.get("blurb", "Local lockout help for drivers and residents who need to get back inside quickly."))}</p>
        <p>Call <strong>{PHONE_DISPLAY}</strong> and we will give you a realistic next step.</p>
      </div>
      <section class="content-block">
        <h2>Vehicle Lockouts in {esc(a["name"])}</h2>
        <p>{esc(detail.get("vehicle", "Mobile unlock help for cars, trucks, and SUVs."))}</p>
        <ul class="text-list">{auto}</ul>
      </section>
      <section class="content-block">
        <h2>Home Lockouts in {esc(a["name"])}</h2>
        <p>{esc(detail.get("home", "Residential lockout help for houses, apartments, condos, and garages."))}</p>
        <ul class="text-list">{home}</ul>
      </section>
      <section class="content-block">
        <h2>Helpful Local Links</h2>
        <ul class="text-list">{useful}</ul>
      </section>
      <section class="content-block"><h2>Nearby Areas</h2><ul class="text-list">{others}</ul></section>
      <section class="content-block"><h2>FAQ</h2><div class="faq-list">{faq_html(faqs)}</div></section>
      <section class="content-block">
        <h2>Lockout Guides</h2>
        <ul class="text-list">
          <li><a href="/resources/locked-out-of-your-car/">Locked out of your car?</a></li>
          <li><a href="/resources/locked-out-of-your-house/">Locked out of your house?</a></li>
          <li><a href="/resources/how-to-get-back-into-car-without-keys/">Get back into a car without keys</a></li>
        </ul>
      </section>
    </div>
    {sidebar()}
  </div>
</section>
<section class="roadside-cta">
  <div class="container roadside-cta-inner">
    <div><p class="eyebrow">{esc(a["name"]).upper()}</p><h2>Locked Out in {esc(a["name"])}?</h2></div>
    <a class="btn btn-primary btn-xl" href="tel:{PHONE_TEL}">CALL {PHONE_DISPLAY}</a>
  </div>
</section>
{footer()}
</body></html>''')


def build_resource_pages():
    cards = "\n".join(
        f'''<a class="resource-card" href="/resources/{r["slug"]}/">
  <div class="resource-card-media" style="background-image:url('{r["image"]}')"></div>
  <div class="resource-card-body">
    <span class="eyebrow">{esc(r["eyebrow"])}</span>
    <h2>{esc(r["title"])}</h2>
    <p>{esc(r["meta_desc"])}</p>
    <span class="service-tile-link">{r["minutes"]} min read →</span>
  </div>
</a>''' for r in RESOURCES
    )
    crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Resource Center", None)])
    item_list = {
        "@context": "https://schema.org", "@type": "ItemList", "name": "Resource Center",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "item": {"@type": "BlogPosting", "headline": r["title"], "url": f"{DOMAIN}/resources/{r['slug']}/", "description": r["meta_desc"], "author": {"@type": "Organization", "name": BRAND}}}
            for i, r in enumerate(RESOURCES, 1)
        ],
    }
    write(ROOT / "resources" / "index.html", f'''{head(
        f"Resource Center | Lockout Guides | {BRAND}",
        "Helpful guides for vehicle and home lockouts in Southwest Florida.",
        f"{DOMAIN}/resources/", schemas=[item_list, crumb_schema],
    )}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("resources")}
<section class="page-hero" id="main">
  <div class="page-hero-media" style="background-image:url('/assets/images/hero.webp')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">RESOURCE CENTER</p>
    <h1>Lockout Guides</h1>
    <p class="page-hero-lead">Practical tips for vehicle and home lockouts.</p>
  </div>
</section>
{crumb_nav}
<section class="section"><div class="container resource-grid">{cards}</div></section>
{footer()}
</body></html>''')

    for r in RESOURCES:
        sections = "".join(f'<section class="content-block"><h2>{esc(h)}</h2><p>{esc(p)}</p></section>' for h, p in r["sections"])
        others = "".join(f'<li><a href="/resources/{o["slug"]}/">{esc(o["title"])}</a></li>' for o in RESOURCES if o["slug"] != r["slug"])
        crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Resources", "/resources/"), (r["title"], None)])
        article = {
            "@context": "https://schema.org", "@type": "Article",
            "headline": r["title"], "description": r["meta_desc"], "image": DOMAIN + r["image"],
            "datePublished": "2026-08-07", "dateModified": TODAY,
            "author": {"@type": "Organization", "name": BRAND},
            "publisher": {"@type": "Organization", "name": BRAND, "logo": {"@type": "ImageObject", "url": DOMAIN + "/LOGO.png"}},
            "mainEntityOfPage": f"{DOMAIN}/resources/{r['slug']}/",
        }
        write(ROOT / "resources" / r["slug"] / "index.html", f'''{head(f"{r['title']} | {BRAND}", r["meta_desc"], f"{DOMAIN}/resources/{r['slug']}/", DOMAIN + r["image"], [article, crumb_schema, faq_schema(r["faqs"])], True)}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("resources")}
<section class="page-hero article-hero" id="main">
  <div class="page-hero-media" style="background-image:url('{r["image"]}')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">{esc(r["eyebrow"])}</p>
    <h1>{esc(r["title"])}</h1>
    <p class="article-meta">{r["minutes"]} min read · Updated {TODAY}</p>
  </div>
</section>
{crumb_nav}
<section class="section page-layout">
  <div class="container page-layout-grid">
    <article class="page-main">
      <div class="content-block intro-block">
        <p>{esc(r["intro"])}</p>
        <p>Need help now? Call <a href="tel:{PHONE_TEL}"><strong>{PHONE_DISPLAY}</strong></a>.</p>
      </div>
      {sections}
      <section class="content-block"><h2>Related Guides</h2><ul class="text-list">{others}</ul></section>
      <section class="content-block"><h2>FAQ</h2><div class="faq-list">{faq_html(r["faqs"])}</div></section>
    </article>
    {sidebar()}
  </div>
</section>
<section class="roadside-cta">
  <div class="container roadside-cta-inner">
    <div><p class="eyebrow">NEED HELP?</p><h2>Call Lockout Pro SWFL</h2></div>
    <a class="btn btn-primary btn-xl" href="tel:{PHONE_TEL}">CALL {PHONE_DISPLAY}</a>
  </div>
</section>
{footer()}
</body></html>''')

    for old, (target, msg) in RESOURCE_REDIRECTS.items():
        write(ROOT / "resources" / old / "index.html", redirect_page(old.replace("-", " ").title(), msg, target, f"{DOMAIN}/resources/{old}/"))


def build_sitemap_and_llms():
    urls = [(f"{DOMAIN}/", "1.0", "weekly"), (f"{DOMAIN}/services/", "0.9", "weekly"), (f"{DOMAIN}/locations/", "0.9", "weekly"), (f"{DOMAIN}/resources/", "0.9", "weekly")]
    for s in SERVICES:
        urls.append((f"{DOMAIN}/services/{s['slug']}/", "0.8", "monthly"))
    for a in AREAS:
        urls.append((f"{DOMAIN}/locations/{a['slug']}/", "0.8", "monthly"))
    for r in RESOURCES:
        urls.append((f"{DOMAIN}/resources/{r['slug']}/", "0.7", "monthly"))
    body = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, pri, freq in urls:
        body.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>")
    body.append("</urlset>")
    write(ROOT / "sitemap.xml", "\n".join(body) + "\n")
    write(ROOT / "robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    write(ROOT / "llms.txt", f"""# {BRAND}

Website:
{DOMAIN}/

Business:
{BRAND}

Description:
Lockout help across Southwest Florida for vehicles and homes — car lockouts, truck & SUV lockouts, trunk lockouts, home lockouts, apartment lockouts, condo lockouts, and garage lockouts.

Phone:
{PHONE_DISPLAY}

Services:
{chr(10).join(f"- {s['name']}: {DOMAIN}/services/{s['slug']}/" for s in SERVICES)}

City Pages:
{chr(10).join(f"- {a['name']}: {DOMAIN}/locations/{a['slug']}/" for a in AREAS)}

Resource Center:
{DOMAIN}/resources/

Articles:
{chr(10).join(f"- {r['title']}: {DOMAIN}/resources/{r['slug']}/" for r in RESOURCES)}

Related Company:
A Good Locksmith (rekeying, installations, key replacement): {AGL}

Website Purpose:
Help people locked out of vehicles or homes in Southwest Florida quickly reach Lockout Pro SWFL.
""")


def main():
    build_service_pages()
    build_location_pages()
    build_resource_pages()
    build_sitemap_and_llms()
    print("Pages generated.")


if __name__ == "__main__":
    main()
