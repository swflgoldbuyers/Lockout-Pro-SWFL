#!/usr/bin/env python3
"""Generate Lockout Pro SWFL multi-page static website."""

from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent
DOMAIN = "https://lockoutproswfl.com"
PHONE_DISPLAY = "(239) 380-5240"
PHONE_TEL = "2393805240"
PHONE_SCHEMA = "+1-239-380-5240"
BRAND = "Lockout Pro SWFL"
TODAY = date.today().isoformat()

AREAS = [
    {"slug": "fort-myers", "name": "Fort Myers", "county": "Lee County"},
    {"slug": "cape-coral", "name": "Cape Coral", "county": "Lee County"},
    {"slug": "naples", "name": "Naples", "county": "Collier County"},
    {"slug": "bonita-springs", "name": "Bonita Springs", "county": "Lee County"},
    {"slug": "estero", "name": "Estero", "county": "Lee County"},
    {"slug": "north-naples", "name": "North Naples", "county": "Collier County"},
    {"slug": "fort-myers-beach", "name": "Fort Myers Beach", "county": "Lee County"},
    {"slug": "lehigh-acres", "name": "Lehigh Acres", "county": "Lee County"},
    {"slug": "san-carlos-park", "name": "San Carlos Park", "county": "Lee County"},
    {"slug": "north-fort-myers", "name": "North Fort Myers", "county": "Lee County"},
]

SERVICES = [
    {
        "slug": "car-lockouts",
        "name": "Car Lockouts",
        "short": "Damage-free vehicle unlocks when your keys are locked inside.",
        "eyebrow": "EMERGENCY SERVICE",
        "h1": "Car Lockout Service Across Southwest Florida",
        "meta_title": "Car Lockouts SWFL | Fast Damage-Free Vehicle Unlock | Lockout Pro",
        "meta_desc": "Locked out of your car in Fort Myers, Cape Coral, Naples or SWFL? Lockout Pro provides fast, damage-free car lockout service 24/7. Call (239) 380-5240.",
        "intro": "Keys on the seat. Door locked. Engine running. Florida heat climbing. A car lockout is an emergency — and Lockout Pro SWFL is built for exactly this moment.",
        "body": [
            ("We're On The Way", "Our mobile automotive locksmiths respond throughout Southwest Florida with professional entry tools designed for modern vehicles. We open cars, trucks, and SUVs carefully — without the pry-bar damage DIY methods often cause."),
            ("When You Should Call Immediately", "Call right away if a child or pet is inside, the engine is running, you're in an unsafe area, or you're stranded after dark. Tell us your vehicle year, make, and model so we arrive prepared."),
            ("What We Unlock", "We handle keys locked in the cabin, trunk-linked lockouts, lockouts with the engine running, and vehicles in parking lots, driveways, workplaces, and roadside locations across SWFL."),
        ],
        "faqs": [
            ("How fast can you unlock my car?", "Response time depends on your location and current calls. When you dial us, we give a realistic arrival estimate for your area."),
            ("Will unlocking damage my door?", "We use professional automotive entry methods intended to minimize risk. Improvised tools are far more likely to damage seals, paint, or linkages."),
            ("Do you unlock cars in Naples and Cape Coral?", "Yes. We cover Fort Myers, Cape Coral, Naples, Estero, Bonita Springs, Lehigh Acres, and surrounding SWFL communities."),
            ("What if my keys are lost, not locked inside?", "Then you likely need lost key replacement and programming — we handle that too."),
        ],
        "related": ["lost-car-keys", "emergency-automotive-locksmith", "trunk-lockouts"],
        "image": "/assets/images/porsche-night.jpg",
    },
    {
        "slug": "lost-car-keys",
        "name": "Lost Car Keys",
        "short": "Replacement keys when your only set is gone.",
        "eyebrow": "KEY REPLACEMENT",
        "h1": "Lost Car Keys? We'll Get You Moving Again",
        "meta_title": "Lost Car Keys SWFL | Replacement Keys On-Site | Lockout Pro",
        "meta_desc": "Lost your only car key in Southwest Florida? Lockout Pro cuts and programs replacement keys on-site for many makes and models. Call (239) 380-5240.",
        "intro": "Losing your only car key is more than inconvenient — it strands you. Lockout Pro SWFL specializes in on-site lost key solutions for drivers across Southwest Florida.",
        "body": [
            ("All-Keys-Lost Solutions", "We diagnose whether you need a traditional cut key, a transponder key, a key fob, a smart key, or a push-to-start system replacement — then create a working solution at your location whenever vehicle support allows."),
            ("What To Have Ready", "Know your vehicle year, make, model, and VIN if available. That information helps us confirm key type and programming requirements before we arrive."),
            ("Prevention After Recovery", "Once you're back on the road, ask about a spare. Most lockout emergencies start with a single-key household."),
        ],
        "faqs": [
            ("Can you make a key if I have zero keys left?", "In many cases yes. All-keys-lost service depends on the vehicle's security system and available programming methods."),
            ("Do I need to go to the dealership?", "Not always. A mobile automotive locksmith can often complete the job on-site for less downtime."),
            ("How long does lost key replacement take?", "It varies by vehicle. Call with your year, make, and model for a clearer estimate."),
            ("Can you help if the key was stolen?", "Yes — tell us immediately so we can discuss replacement and security considerations for your vehicle."),
        ],
        "related": ["car-key-replacement", "key-fob-programming", "duplicate-car-keys"],
        "image": "/assets/images/car-keys.jpg",
    },
    {
        "slug": "car-key-replacement",
        "name": "Car Key Replacement",
        "short": "Cut and programmed replacement keys for many vehicles.",
        "eyebrow": "AUTOMOTIVE KEYS",
        "h1": "Car Key Replacement Throughout SWFL",
        "meta_title": "Car Key Replacement SWFL | Cut & Programmed Keys | Lockout Pro",
        "meta_desc": "Need a replacement car key in Fort Myers or SW Florida? Lockout Pro provides mobile car key cutting and programming. Call (239) 380-5240.",
        "intro": "Whether your key snapped, vanished, or stopped communicating with the vehicle, Lockout Pro SWFL provides mobile car key replacement built around modern automotive security.",
        "body": [
            ("More Than Cutting Metal", "Today's keys often include transponder chips, remote buttons, or proximity sensors. Replacement means cutting and programming — not just duplicating a blade."),
            ("Mobile Convenience", "We come to your home, workplace, or roadside location across Fort Myers, Cape Coral, Naples, and nearby communities."),
            ("Right Key For Your Vehicle", "From basic keys to smart and push-to-start systems, we match the service to your specific year, make, and model."),
        ],
        "faqs": [
            ("Can every car key be replaced on-site?", "Most common vehicles can. Some specialty or newer systems may require additional steps — call to confirm."),
            ("Is dealership the only option?", "No. Mobile automotive locksmiths regularly replace and program keys outside the dealership."),
            ("Should I get a spare at the same time?", "Yes. A spare is the cheapest insurance against the next lockout."),
            ("What if only the remote buttons failed?", "You may need fob repair, battery service, or full key fob programming rather than a full key blade replacement."),
        ],
        "related": ["key-fob-programming", "smart-keys", "push-to-start-keys"],
        "image": "/assets/images/key-fob.jpg",
    },
    {
        "slug": "key-fob-programming",
        "name": "Key Fob Programming",
        "short": "Program remotes and fobs to your vehicle.",
        "eyebrow": "PROGRAMMING",
        "h1": "Key Fob Programming For Modern Vehicles",
        "meta_title": "Key Fob Programming SWFL | Remote & Fob Setup | Lockout Pro",
        "meta_desc": "Need key fob programming in Southwest Florida? Lockout Pro programs remotes and fobs for many makes and models. Call (239) 380-5240.",
        "intro": "A key fob that won't lock, unlock, or start the car leaves you stuck. Lockout Pro SWFL programs and replaces key fobs for drivers across Southwest Florida.",
        "body": [
            ("Why Fobs Fail", "Dead batteries, dropped remotes, water damage, button wear, and lost fobs are common. Sometimes the fob hardware is fine and only needs programming; other times replacement is required."),
            ("Professional Programming Equipment", "Modern vehicles verify encrypted signals between fob and immobilizer. We use automotive locksmith equipment designed for these systems."),
            ("Brands We Commonly Work With", "We service many popular domestic, Asian, and European brands used throughout SWFL. Call with your vehicle details to confirm support."),
        ],
        "faqs": [
            ("My fob suddenly stopped working — is it the battery?", "Often yes. If a new battery doesn't restore function, programming or replacement may be needed."),
            ("Can you program a fob I bought online?", "Sometimes. Compatibility and security protocols vary. Bring vehicle details when you call."),
            ("Do you program smart keys too?", "Yes — see our smart key and push-to-start services for proximity systems."),
            ("How do I know if I need programming or a new fob?", "We'll diagnose based on symptoms, battery state, and vehicle response."),
        ],
        "related": ["smart-keys", "push-to-start-keys", "car-key-replacement"],
        "image": "/assets/images/key-fob.jpg",
    },
    {
        "slug": "smart-keys",
        "name": "Smart Keys",
        "short": "Proximity smart key replacement and programming.",
        "eyebrow": "SMART SYSTEMS",
        "h1": "Smart Key Replacement & Programming",
        "meta_title": "Smart Key Replacement SWFL | Proximity Keys | Lockout Pro",
        "meta_desc": "Lost or failed smart key in SWFL? Lockout Pro replaces and programs proximity smart keys for many vehicles. Call (239) 380-5240.",
        "intro": "Smart keys unlock and start your vehicle without a traditional blade turn. When one fails or disappears, you need an automotive specialist — not a hardware-store duplicate.",
        "body": [
            ("What Makes A Key Smart", "Proximity detection, encrypted authentication, and push-button start integration make smart keys more complex than standard remotes."),
            ("On-Site Smart Key Help", "Lockout Pro SWFL provides mobile smart key replacement and programming across Southwest Florida whenever your vehicle platform is supported."),
            ("Don't Wait Until You're Stranded", "If your smart key works intermittently, schedule service before a complete failure leaves you locked out."),
        ],
        "faqs": [
            ("Can a locksmith make smart keys?", "Yes — automotive locksmiths with the right equipment regularly replace and program smart keys."),
            ("Is a smart key the same as a push-to-start key?", "Often related, but not identical. Push-to-start vehicles typically use smart/proximity keys."),
            ("What if my smart key was damaged by water?", "Water damage is common. We can discuss replacement options for your specific vehicle."),
            ("Do I need two smart keys programmed?", "Having two is strongly recommended so one failure doesn't strand you."),
        ],
        "related": ["push-to-start-keys", "key-fob-programming", "lost-car-keys"],
        "image": "/assets/images/car-interior.jpg",
    },
    {
        "slug": "push-to-start-keys",
        "name": "Push-To-Start Keys",
        "short": "Push-button start key replacement and programming.",
        "eyebrow": "PUSH-TO-START",
        "h1": "Push-To-Start Key Service In SWFL",
        "meta_title": "Push-To-Start Keys SWFL | Replacement & Programming | Lockout Pro",
        "meta_desc": "Push-to-start key not working in Fort Myers or SWFL? Lockout Pro replaces and programs push-button start keys. Call (239) 380-5240.",
        "intro": "Push-to-start convenience is only convenient when the key authenticates. When it doesn't, Lockout Pro SWFL helps restore access with professional programming.",
        "body": [
            ("Common Push-To-Start Failures", "Weak fob batteries, damaged antennas, lost proximity keys, and failed immobilizer communication can all prevent starting."),
            ("Replacement Done Right", "A working push-to-start key must be correctly programmed to your vehicle's security system — not simply ordered online and hoped for."),
            ("Mobile Service Across SWFL", "We come to you in Fort Myers, Naples, Cape Coral, Estero, Bonita Springs, and surrounding areas."),
        ],
        "faqs": [
            ("Can a locksmith replace push-to-start keys?", "Yes. Automotive locksmiths routinely handle push-to-start key replacement and programming."),
            ("Why does my car say key not detected?", "Common causes include a dead fob battery, interference, or a failing proximity key."),
            ("Can I start the car with a dead fob battery?", "Some vehicles allow a backup start method. Check your owner's manual or call us for guidance."),
            ("Should I keep a spare push-to-start key?", "Absolutely. These systems are expensive to replace in an emergency."),
        ],
        "related": ["smart-keys", "key-fob-programming", "ignition-repair"],
        "image": "/assets/images/car-interior.jpg",
    },
    {
        "slug": "broken-car-key-extraction",
        "name": "Broken Car Key Extraction",
        "short": "Safe removal of keys broken in door or ignition.",
        "eyebrow": "EXTRACTION",
        "h1": "Broken Car Key Extraction",
        "meta_title": "Broken Car Key Extraction SWFL | Ignition & Door | Lockout Pro",
        "meta_desc": "Key broken in your ignition or door lock? Lockout Pro extracts broken car keys carefully and can cut a replacement. Call (239) 380-5240.",
        "intro": "A key snapped off in the ignition or door lock can shut your day down instantly. Forcing it deeper usually makes extraction harder — call a pro.",
        "body": [
            ("Careful Extraction First", "We remove the broken piece with professional extraction tools designed to protect wafers, tumblers, and surrounding hardware."),
            ("Then Restore Access", "After extraction, we can often cut a replacement key and address related ignition or lock concerns."),
            ("Why Keys Break", "Worn keys, sticky ignitions, excessive force, and age-related metal fatigue are common causes across Southwest Florida vehicles."),
        ],
        "faqs": [
            ("Should I try to dig the key out myself?", "No. Improvised picks can push fragments deeper or damage the cylinder."),
            ("Can you extract a key from the ignition?", "Yes — ignition and door lock extractions are core automotive locksmith work."),
            ("Will I need a new ignition?", "Not always. Many extractions leave the cylinder usable. We'll assess after removal."),
            ("Can you make a new key from the broken pieces?", "Often yes, especially if enough of the original key remains or vehicle codes are available."),
        ],
        "related": ["ignition-repair", "car-key-replacement", "duplicate-car-keys"],
        "image": "/assets/images/automotive-work.jpg",
    },
    {
        "slug": "ignition-repair",
        "name": "Ignition Repair",
        "short": "Help when the key won't turn or the ignition fails.",
        "eyebrow": "IGNITION SERVICE",
        "h1": "Automotive Ignition Repair Assistance",
        "meta_title": "Ignition Repair SWFL | Key Won't Turn | Lockout Pro",
        "meta_desc": "Key won't turn in the ignition in SW Florida? Lockout Pro provides automotive ignition repair assistance and related key services. Call (239) 380-5240.",
        "intro": "When the key won't turn, sticks, or the ignition cylinder feels wrong, waiting often makes it worse. Lockout Pro SWFL helps diagnose and restore ignition access.",
        "body": [
            ("Signs Of Ignition Trouble", "Difficulty turning the key, intermittent start issues, keys sticking, grinding sensations, or needing to jiggle the steering wheel repeatedly are warning signs."),
            ("Repair Vs Replacement", "Some issues are cylinder-related; others involve the key, tumblers, or related components. We assess the practical path forward for your vehicle."),
            ("Don't Force It", "Forcing a stuck ignition can break the key or worsen internal damage. Call before it becomes an extraction emergency."),
        ],
        "faqs": [
            ("Why won't my key turn in the ignition?", "Common causes include steering lock tension, worn tumblers, damaged keys, or cylinder failure."),
            ("Is ignition repair the same as a new car key?", "No — but worn keys and failing cylinders often appear together."),
            ("Do you work on push-to-start ignitions?", "Push-to-start systems involve different components. Call with your vehicle details."),
            ("Can you help if the key spins freely?", "A freely spinning key often indicates serious cylinder or linkage issues — call for assessment."),
        ],
        "related": ["broken-car-key-extraction", "car-key-replacement", "push-to-start-keys"],
        "image": "/assets/images/automotive-work.jpg",
    },
    {
        "slug": "duplicate-car-keys",
        "name": "Duplicate Car Keys",
        "short": "Spare keys cut and programmed before you need them.",
        "eyebrow": "SPARES",
        "h1": "Duplicate Car Keys & Spares",
        "meta_title": "Duplicate Car Keys SWFL | Spare Keys Cut & Programmed | Lockout Pro",
        "meta_desc": "Get a spare car key before you're locked out. Lockout Pro duplicates and programs car keys across Southwest Florida. Call (239) 380-5240.",
        "intro": "The best time to get a spare car key is before you need one. Lockout Pro SWFL helps Southwest Florida drivers add duplicates for peace of mind.",
        "body": [
            ("One Key Is A Risk", "Households with a single working key are one drop, one lockout, or one lost fob away from an emergency service call."),
            ("Proper Duplication", "Many modern keys require programming after cutting. A blade-only copy may unlock a door but fail to start the engine."),
            ("Schedule Before Emergency Rates", "Planned spare keys are calmer, clearer, and usually more convenient than all-keys-lost emergencies."),
        ],
        "faqs": [
            ("Can any car key be duplicated?", "Most can, but transponder and smart keys need proper programming."),
            ("How many spares should I have?", "At least one reliable spare kept separately from your daily key."),
            ("Can you duplicate from the VIN if I only have one key?", "Often yes — and duplicating while you still have a working key is ideal."),
            ("Do motorcycle keys work the same way?", "Some do; see our motorcycle key service for bike-specific help."),
        ],
        "related": ["car-key-replacement", "lost-car-keys", "motorcycle-keys"],
        "image": "/assets/images/car-keys.jpg",
    },
    {
        "slug": "motorcycle-keys",
        "name": "Motorcycle Keys",
        "short": "Motorcycle key cutting and replacement help.",
        "eyebrow": "MOTORCYCLE",
        "h1": "Motorcycle Key Replacement In SWFL",
        "meta_title": "Motorcycle Keys SWFL | Bike Key Replacement | Lockout Pro",
        "meta_desc": "Lost or broken motorcycle key in Southwest Florida? Lockout Pro helps with motorcycle key cutting and replacement. Call (239) 380-5240.",
        "intro": "A lost motorcycle key can leave your bike stuck at home, work, or a trailhead. Lockout Pro SWFL provides motorcycle key assistance for many makes.",
        "body": [
            ("Bike Keys Are Different", "Motorcycle locks and keyways vary widely. Some use simple mechanical keys; others include chips or unique profiles."),
            ("What Helps Us Help You", "Year, make, model, and any remaining key code information speed up the process."),
            ("Don't Force A Wrong Key", "Trying random keys or improvised tools can damage ignition switches and forks."),
        ],
        "faqs": [
            ("Can you make a motorcycle key with no original?", "Often yes, depending on the bike and available codes or methods."),
            ("Do you come to my location?", "Yes — mobile service across our SWFL coverage area."),
            ("Can you duplicate a motorcycle key while I still have one?", "Yes, and that's the ideal time."),
            ("What about ATV or scooter keys?", "Call with details — many powersports keys can be supported."),
        ],
        "related": ["duplicate-car-keys", "lost-car-keys", "car-key-replacement"],
        "image": "/assets/images/sports-car.jpg",
    },
    {
        "slug": "trunk-lockouts",
        "name": "Trunk Lockouts",
        "short": "Keys locked in the trunk? We help recover access.",
        "eyebrow": "TRUNK ACCESS",
        "h1": "Trunk Lockout Service",
        "meta_title": "Trunk Lockouts SWFL | Keys Locked In Trunk | Lockout Pro",
        "meta_desc": "Keys locked in the trunk in Fort Myers or SWFL? Lockout Pro provides professional trunk lockout assistance. Call (239) 380-5240.",
        "intro": "Keys in the trunk and no cabin access — or a trunk that won't release — needs careful automotive locksmith work, not a crowbar.",
        "body": [
            ("Cabin First Or Trunk Direct", "Some vehicles allow cabin entry that restores trunk release. Others need a trunk-focused approach. We choose the method that fits your vehicle."),
            ("Protect Latches And Seals", "Forced entry can destroy trunk latches and weather seals. Professional methods prioritize controlled access."),
            ("Common Situations", "Grocery runs, beach days, and airport parking lots are frequent trunk-lockout scenes across Southwest Florida."),
        ],
        "faqs": [
            ("Can you open a trunk without keys?", "In many cases yes, using vehicle-appropriate techniques."),
            ("My keys are in the trunk and the car is locked — can you help?", "Yes. That's a common emergency call for us."),
            ("Will you damage the trunk?", "Our goal is non-destructive access whenever possible."),
            ("What if the electronic trunk release failed?", "Tell us the symptoms — mechanical and electronic failures need different approaches."),
        ],
        "related": ["car-lockouts", "emergency-automotive-locksmith", "lost-car-keys"],
        "image": "/assets/images/luxury-car.jpg",
    },
    {
        "slug": "fleet-vehicle-locksmith",
        "name": "Fleet Vehicle Locksmith",
        "short": "Key and lockout support for business fleets.",
        "eyebrow": "FLEET SERVICES",
        "h1": "Fleet Vehicle Locksmith Services",
        "meta_title": "Fleet Vehicle Locksmith SWFL | Business Key Support | Lockout Pro",
        "meta_desc": "Need fleet vehicle locksmith support in SWFL? Lockout Pro helps businesses with lockouts, keys, and fob programming. Call (239) 380-5240.",
        "intro": "Downtime costs money. Lockout Pro SWFL helps Southwest Florida businesses keep fleet vehicles moving with lockout response, key replacement, and fob programming.",
        "body": [
            ("Built For Business Continuity", "When a work truck, van, or company car is sidelined by a lockout or lost key, we prioritize practical turnaround."),
            ("Services Fleets Use Most", "Emergency unlocks, spare key programs, fob replacements, and ignition-related assistance for supported vehicles."),
            ("One Call Coordination", "Share vehicle details and location — we'll coordinate mobile service across Lee and Collier County coverage areas."),
        ],
        "faqs": [
            ("Do you work with small business fleets?", "Yes — from a few vehicles to larger local fleets."),
            ("Can you create spare keys for multiple vehicles?", "Yes. Planned spare programs reduce emergency downtime."),
            ("Do you invoice businesses?", "Call to discuss your needs and service process."),
            ("What vehicle types do you support?", "Many cars, trucks, and vans used in SWFL fleets. Confirm by year, make, and model."),
        ],
        "related": ["car-lockouts", "duplicate-car-keys", "key-fob-programming"],
        "image": "/assets/images/driving.jpg",
    },
    {
        "slug": "emergency-automotive-locksmith",
        "name": "Emergency Automotive Locksmith",
        "short": "24/7 mobile automotive locksmith response.",
        "eyebrow": "24/7 EMERGENCY",
        "h1": "Emergency Automotive Locksmith — 24/7",
        "meta_title": "Emergency Automotive Locksmith SWFL | 24/7 Mobile | Lockout Pro",
        "meta_desc": "Emergency automotive locksmith in Southwest Florida. 24/7 mobile help for lockouts, lost keys, and key failures. Call Lockout Pro at (239) 380-5240.",
        "intro": "Locked out at 2 a.m.? Key failed in a dark parking lot? Lockout Pro SWFL is the emergency automotive locksmith built for urgent, mobile response.",
        "body": [
            ("Automotive Only. Emergency Ready.", "We don't dilute focus across home and office locks. Our attention stays on vehicles — lockouts, keys, fobs, ignitions, and roadside automotive access."),
            ("What Counts As An Emergency", "Keys locked inside, all keys lost, broken keys, failed fobs, trunk lockouts, and ignition failures that leave you stranded."),
            ("Clear Communication", "When you call, we confirm location, vehicle details, and a realistic arrival window so you're not left guessing."),
        ],
        "faqs": [
            ("Are you really available 24/7?", "Yes — emergency automotive locksmith service around the clock across our SWFL area."),
            ("How do I get faster help?", "Call with exact location, vehicle year/make/model, and whether anyone is inside the vehicle."),
            ("Do you only do automotive?", "Yes. For residential or commercial locksmith needs, visit A Good Locksmith."),
            ("What areas do you cover after hours?", "Fort Myers, Cape Coral, Naples, Estero, Bonita Springs, and surrounding Southwest Florida communities."),
        ],
        "related": ["car-lockouts", "lost-car-keys", "key-fob-programming"],
        "image": "/assets/images/porsche-night.jpg",
    },
]

RESOURCES = [
    {
        "slug": "locked-out-of-your-car",
        "title": "Locked Out Of Your Car? Here's What To Do",
        "eyebrow": "EMERGENCY GUIDE",
        "meta_desc": "Locked your keys in the car in SWFL? Stay safe, avoid damage, and get professional help fast with this Lockout Pro guide.",
        "minutes": 6,
        "image": "/assets/images/porsche-night.jpg",
        "intro": "A car lockout rarely happens at a convenient time. Keys sit on the seat, a fob dies in a parking lot, or someone hits lock while you're outside with grocery bags. The next few minutes matter — the wrong DIY move can crack a weather seal, bend a linkage, or turn a stressful afternoon into a body-shop visit.",
        "sections": [
            ("1. Check Safety First", "If a child or pet is inside, call for help immediately and tell the dispatcher and locksmith. Move to a safe place near the vehicle. In heat, prioritize shade and hydration while you wait."),
            ("2. Confirm It's Actually Locked", "Try every door. Check for a spare. Ask if anyone nearby has a second fob. On some vehicles, the trunk or app may offer a path — but don't force anything."),
            ("3. Avoid DIY Entry Tools", "Coat hangers, knives, and viral 'unlock hacks' commonly damage weatherstripping, wiring, paint, and side-curtain airbag components. Modern cars are not designed for improvised entry."),
            ("4. Call A Mobile Automotive Locksmith", "Provide your exact location, vehicle year/make/model, and whether the engine is running. Lockout Pro SWFL specializes in damage-conscious vehicle entry across Southwest Florida."),
            ("5. After You're Back In", "Inspect seals briefly, confirm nothing was left that caused the lockout, and seriously consider a spare key. One working key is a future emergency waiting to happen."),
        ],
        "faqs": [
            ("Can a locksmith unlock my car without damaging it?", "In most lockout situations, yes. Professionals use vehicle-appropriate tools and aim for non-destructive entry."),
            ("What if my keys are lost, not locked inside?", "You likely need key replacement and possibly programming rather than a simple unlock."),
            ("Should I try to unlock the car myself?", "If everyone is safe, avoid improvised tools. DIY methods commonly cause expensive damage."),
        ],
    },
    {
        "slug": "lost-car-keys-guide",
        "title": "Lost Your Car Keys? Complete Guide",
        "eyebrow": "KEY REPLACEMENT",
        "meta_desc": "Lost your car keys in Southwest Florida? Learn what to do next, what information helps, and how mobile key replacement works.",
        "minutes": 7,
        "image": "/assets/images/car-keys.jpg",
        "intro": "Losing your car keys triggers a unique kind of panic — especially if it was your only set. This guide walks Southwest Florida drivers through the practical next steps, from searching smart to getting a programmed replacement.",
        "sections": [
            ("Retrace With A System", "Check pockets, bags, under seats (if accessible), recent stores, and the last place you used the remote. Ask nearby businesses to check lost-and-found before ordering a replacement."),
            ("Gather Vehicle Details", "Year, make, model, and VIN help an automotive locksmith identify key type — blade only, transponder, fob, smart key, or push-to-start."),
            ("Understand Modern Keys", "Many keys must be programmed to start the engine. A hardware-store duplicate may open a door and still leave you stranded."),
            ("Call For Mobile Replacement", "Lockout Pro SWFL can often create and program a replacement at your location, reducing dealership wait times and tow costs."),
            ("Add A Spare Immediately", "Once restored, duplicate a spare and store it separately. The second key is the cheapest lockout prevention available."),
        ],
        "faqs": [
            ("Can keys be made with zero originals left?", "Often yes through all-keys-lost procedures, depending on the vehicle."),
            ("Do I need the dealership?", "Not always. Mobile automotive locksmiths handle many replacements on-site."),
            ("What if the keys were stolen?", "Tell the locksmith — security and replacement considerations may change."),
        ],
    },
    {
        "slug": "how-much-does-a-car-locksmith-cost",
        "title": "How Much Does A Car Locksmith Cost?",
        "eyebrow": "PRICING GUIDE",
        "meta_desc": "What affects car locksmith pricing in SWFL? Learn the factors behind lockouts, key replacement, and fob programming costs.",
        "minutes": 5,
        "image": "/assets/images/automotive-work.jpg",
        "intro": "Car locksmith pricing isn't one flat number — because unlocking a 2008 sedan is not the same job as programming a 2022 push-to-start smart key. Here's what actually drives cost in Southwest Florida.",
        "sections": [
            ("Service Type Matters Most", "A straightforward lockout usually costs less than all-keys-lost replacement. Fob programming, ignition work, and smart keys involve more time and equipment."),
            ("Vehicle Year, Make, And Model", "Luxury brands, newer immobilizer systems, and uncommon keyways can require specialized tools or parts."),
            ("Time And Location", "After-hours emergencies, distant locations, and high-demand periods can affect response pricing. Clear communication when you call helps set expectations."),
            ("Parts Vs Labor", "Some jobs are mostly skilled labor. Others require key blanks, fobs, or components. Ask what's included before work begins."),
            ("How To Avoid Surprise Pricing", "Be wary of quotes that sound too low without asking for vehicle details. Provide accurate information and ask for a clear estimate range."),
        ],
        "faqs": [
            ("Why won't anyone give me an exact price by text?", "Because vehicle security systems vary. Accurate estimates need year, make, model, and symptom details."),
            ("Is the cheapest quote the best deal?", "Not if it leads to damage, incomplete programming, or bait-and-switch pricing."),
            ("Can I lower cost somehow?", "Having a spare key, acting before total failure, and calling promptly often reduce total hassle and cost."),
        ],
    },
    {
        "slug": "key-fob-stopped-working",
        "title": "Key Fob Stopped Working?",
        "eyebrow": "TROUBLESHOOTING",
        "meta_desc": "Key fob suddenly stopped working? Try these steps before replacing it, and know when to call Lockout Pro SWFL.",
        "minutes": 5,
        "image": "/assets/images/key-fob.jpg",
        "intro": "A silent key fob can mean a $3 battery — or a failed remote that needs programming. Work through simple checks first, then call a professional if the vehicle still won't respond.",
        "sections": [
            ("Replace The Battery First", "Weak batteries cause intermittent range loss and sudden failure. Use the correct battery type and seat it firmly."),
            ("Check For Physical Damage", "Cracked housings, sticky buttons, and water exposure are common in Florida heat, storms, and beach days."),
            ("Rule Out Vehicle-Side Issues", "If a second fob also fails, the issue may involve the vehicle receiver or battery — not only the remote."),
            ("Programming And Replacement", "When hardware is fine but the car ignores the fob, programming may be required. If the fob is dead, replacement plus programming is the path."),
            ("Prevention Tips", "Keep a spare fob, avoid tossing remotes into wet gear bags, and replace batteries at the first sign of reduced range."),
        ],
        "faqs": [
            ("Can a locksmith program a fob I bought online?", "Sometimes, if it's the correct compatible unit for your vehicle."),
            ("Why does my fob work only when I'm next to the door?", "Usually a weak battery or failing antenna/transmitter."),
            ("Is a smart key different from a fob?", "Smart/proximity keys are a related but more advanced category."),
        ],
    },
    {
        "slug": "can-a-locksmith-replace-push-to-start-keys",
        "title": "Can A Locksmith Replace Push-To-Start Keys?",
        "eyebrow": "SMART KEYS",
        "meta_desc": "Yes — automotive locksmiths can often replace and program push-to-start keys. Learn how the process works in SWFL.",
        "minutes": 6,
        "image": "/assets/images/car-interior.jpg",
        "intro": "Yes. A qualified automotive locksmith can often replace and program push-to-start keys without a dealership visit. Here's what drivers in Southwest Florida should know.",
        "sections": [
            ("Push-To-Start Needs Authentication", "The button only works when a programmed proximity key is recognized. Lost, damaged, or unprogrammed keys won't start the vehicle."),
            ("What The Locksmith Needs", "Vehicle year, make, model, and proof of ownership help confirm the correct key type and programming procedure."),
            ("On-Site Programming", "Many vehicles can be programmed mobile with professional equipment. Some platforms are more complex — confirmation by phone avoids surprises."),
            ("Dead Fob Battery Myths", "A dead battery can mimic a failed key. Some cars allow a backup start method with the fob held to a button or mark — check your manual."),
            ("Get A Second Key", "Push-to-start replacements are not the job you want to do twice under emergency pressure. Add a spare once service is complete."),
        ],
        "faqs": [
            ("Is dealership required for push-to-start keys?", "Not always. Many keys are handled by mobile automotive locksmiths."),
            ("How long does programming take?", "It varies by vehicle. Call with details for a better estimate."),
            ("Can you clone my existing push-to-start key?", "Processes differ by manufacturer. Sometimes duplication from an existing key is possible; sometimes all keys must be programmed in a set."),
        ],
    },
    {
        "slug": "prevent-locking-keys-in-your-car",
        "title": "How To Prevent Locking Keys In Your Car",
        "eyebrow": "PREVENTION",
        "meta_desc": "Practical habits to stop locking your keys in the car — plus why a spare key is still essential for SWFL drivers.",
        "minutes": 4,
        "image": "/assets/images/driving.jpg",
        "intro": "Most lockouts are preventable. A few habits — and one spare key — dramatically reduce the odds you'll be standing in a hot parking lot waiting for help.",
        "sections": [
            ("Never Leave The Fob On The Seat", "It sounds obvious until groceries, kids, or beach gear distract you. Keep the fob in a fixed pocket or bag pocket every time."),
            ("Watch Soft-Close And Auto-Lock Features", "Some vehicles lock automatically. Learn your model's behavior so it doesn't lock behind you with the key inside."),
            ("Use A Spare Strategy", "Keep a properly programmed spare at home or with a trusted person. An unprogrammed blade is not enough for many cars."),
            ("Battery Awareness", "A dying fob battery can create weird lock/unlock behavior that contributes to lockouts. Replace early."),
            ("Phone As Backup — With Limits", "Manufacturer apps can help on some newer cars, but connectivity fails. Don't treat an app as your only spare."),
        ],
        "faqs": [
            ("What's the #1 lockout prevention tip?", "Own a working spare key stored separately from your daily key."),
            ("Do auto-lock features cause lockouts?", "They can, especially when drivers are unfamiliar with a vehicle."),
            ("Should I hide a key on the car?", "Magnetic hide-a-keys are risky. A secure spare at home is safer."),
        ],
    },
    {
        "slug": "signs-ignition-cylinder-failing",
        "title": "Signs Your Ignition Cylinder Is Failing",
        "eyebrow": "IGNITION",
        "meta_desc": "Key hard to turn? Ignition sticking? Learn the warning signs of a failing ignition cylinder before you get stranded.",
        "minutes": 5,
        "image": "/assets/images/automotive-work.jpg",
        "intro": "Ignition cylinders rarely fail without warning. Catching the signs early can mean a repair instead of a broken key extraction in a parking lot.",
        "sections": [
            ("The Key Is Hard To Turn", "Increased resistance, especially when hot or cold, often points to worn tumblers or a degrading cylinder."),
            ("You Have To Jiggle Constantly", "Occasional steering-lock tension is normal. Constant jiggling to find a 'sweet spot' is not."),
            ("Key Sticks On Removal", "Difficulty inserting or removing the key suggests internal wear that can worsen quickly."),
            ("Intermittent Starting", "If accessory power behaves oddly or the key position feels mushy, have it inspected before a roadside failure."),
            ("Don't Force A Sticky Ignition", "Forcing is how keys snap off inside the cylinder. Call Lockout Pro SWFL for assessment and extraction if needed."),
        ],
        "faqs": [
            ("Can a worn key mimic ignition failure?", "Yes. A worn key and a worn cylinder often appear together."),
            ("Is a push-to-start car immune?", "No — those systems have different failure modes, but they still fail."),
            ("Should I keep driving if it's sticky?", "You can get stranded mid-errand. Schedule service promptly."),
        ],
    },
    {
        "slug": "spare-car-keys-every-driver",
        "title": "Spare Car Keys: Why Every Driver Should Have One",
        "eyebrow": "SPARES",
        "meta_desc": "Why every Southwest Florida driver needs a spare car key — and how to get one programmed correctly.",
        "minutes": 4,
        "image": "/assets/images/car-keys.jpg",
        "intro": "A spare car key is not a luxury. It's the simplest way to avoid emergency lockouts, lost-key chaos, and expensive all-keys-lost programming.",
        "sections": [
            ("One Key = One Point Of Failure", "Drop it in a lake, leave it at the beach, or lock it inside — and your day stops."),
            ("Modern Keys Need Programming", "A spare must actually start the car. That often means cutting plus programming, not a bargain blade copy."),
            ("Best Time To Get A Spare", "While you still have a working key. All-keys-lost jobs are harder and usually more stressful."),
            ("Where To Keep It", "At home or with a trusted person — not inside the vehicle."),
            ("SWFL Reality Check", "Heat, beaches, tourism, and busy parking lots make lockouts common. A spare is local common sense."),
        ],
        "faqs": [
            ("How many spare keys do I need?", "At least one reliable spare is the baseline."),
            ("Can Lockout Pro make spares mobile?", "Yes — call with your vehicle year, make, and model."),
            ("Are OEM keys required?", "Quality compatible keys programmed correctly are what matter. Ask us what's appropriate for your vehicle."),
        ],
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def header(active: str = "") -> str:
    def cls(name):
        return ' class="is-active"' if active == name else ""

    return f'''<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="/" aria-label="{BRAND} home">
      <img src="/LOGO.png" alt="{BRAND}" class="brand-logo" width="72" height="72">
      <span class="brand-text">
        <span class="brand-name"><span class="brand-lockout">LOCKOUT</span> <span class="brand-pro">PRO</span></span>
        <span class="brand-sub">SWFL Automotive</span>
      </span>
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
      <span class="header-phone-label">24/7 Call Now</span>
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
    <a href="/resources/">Resource Center</a>
    <a href="/#faq">FAQ</a>
    <a href="/#contact">Contact</a>
    <a class="mobile-call" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  </div>
</header>'''


def footer() -> str:
    service_links = "\n".join(
        f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])}</a></li>'
        for s in SERVICES[:6]
    )
    area_links = "\n".join(
        f'<li><a href="/locations/{a["slug"]}/">{esc(a["name"])}</a></li>'
        for a in AREAS[:6]
    )
    return f'''<footer class="site-footer" id="contact">
  <div class="container footer-grid">
    <div class="footer-brand">
      <a class="brand footer-brand-link" href="/">
        <img src="/LOGO.png" alt="{BRAND}" width="64" height="64">
        <span>
          <span class="brand-name"><span class="brand-lockout">LOCKOUT</span> <span class="brand-pro">PRO</span></span>
          <span class="brand-sub">Southwest Florida</span>
        </span>
      </a>
      <p>Mobile automotive locksmith specializing in emergency lockouts, lost keys, key fob programming, and ignition help across Southwest Florida.</p>
      <a class="footer-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <p class="footer-hours">Available 24/7 · Automotive Only</p>
    </div>
    <div>
      <h3>Services</h3>
      <ul>{service_links}
        <li><a href="/services/">All Services →</a></li>
      </ul>
    </div>
    <div>
      <h3>Service Areas</h3>
      <ul>{area_links}
        <li><a href="/locations/">All Areas →</a></li>
      </ul>
    </div>
    <div>
      <h3>Need Home Or Business Locks?</h3>
      <p>Looking for residential or commercial locksmith service?</p>
      <a class="footer-outlink" href="https://agoodlocksmith.com" rel="noopener noreferrer" target="_blank">Visit A Good Locksmith →</a>
      <h3 class="footer-spaced">Resources</h3>
      <ul>
        <li><a href="/resources/">Resource Center</a></li>
        <li><a href="/resources/locked-out-of-your-car/">Locked Out Guide</a></li>
        <li><a href="/resources/how-much-does-a-car-locksmith-cost/">Pricing Guide</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <p>© {date.today().year} {BRAND}. All rights reserved.</p>
      <p>Automotive locksmith · Southwest Florida</p>
    </div>
  </div>
</footer>
<a href="tel:{PHONE_TEL}" class="sticky-call" aria-label="Call {BRAND} now">
  <span class="sticky-call-kicker">Locked Out?</span>
  <span class="sticky-call-num">CALL {PHONE_DISPLAY}</span>
</a>
<script src="/script.js" defer></script>'''


def head(
    title: str,
    description: str,
    canonical: str,
    active_theme: str = "#FF7A00",
    og_image: str = f"{DOMAIN}/LOGO.png",
    schemas: list | None = None,
    article: bool = False,
):
    schema_html = ""
    if schemas:
        for schema in schemas:
            import json
            schema_html += (
                '\n<script type="application/ld+json">\n'
                + json.dumps(schema, indent=2)
                + "\n</script>"
            )
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
<meta name="theme-color" content="{active_theme}">
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


def breadcrumbs(items: list[tuple[str, str | None]]) -> str:
    lis = []
    schema_items = []
    for i, (name, href) in enumerate(items, 1):
        if href:
            lis.append(f'<li><a href="{href}">{esc(name)}</a></li>')
            schema_items.append(
                {
                    "@type": "ListItem",
                    "position": i,
                    "name": name,
                    "item": DOMAIN + href if href.startswith("/") else href,
                }
            )
        else:
            lis.append(f'<li aria-current="page"><span>{esc(name)}</span></li>')
            schema_items.append({"@type": "ListItem", "position": i, "name": name})
    nav = f'''<div class="container breadcrumb-wrap">
<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>
</div>'''
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": schema_items,
    }
    return nav, schema


def sidebar(current_service: str | None = None) -> str:
    links = "\n".join(
        '<li><a href="/services/{slug}/"{cls}>{name}</a></li>'.format(
            slug=s["slug"],
            cls=' class="current"' if current_service == s["slug"] else "",
            name=esc(s["name"]),
        )
        for s in SERVICES
    )
    areas = "\n".join(
        f'<li><a href="/locations/{a["slug"]}/">{esc(a["name"])}</a></li>'
        for a in AREAS[:8]
    )
    return f'''<aside class="page-sidebar">
  <div class="sidebar-card sidebar-cta">
    <p class="sidebar-kicker">Need Help Now?</p>
    <a class="sidebar-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
    <a class="btn btn-primary btn-block" href="tel:{PHONE_TEL}">Call Now</a>
    <p class="sidebar-note">24/7 mobile automotive locksmith</p>
  </div>
  <div class="sidebar-card">
    <h3>Services</h3>
    <ul class="sidebar-links">{links}</ul>
  </div>
  <div class="sidebar-card">
    <h3>Areas</h3>
    <ul class="sidebar-links">{areas}</ul>
  </div>
</aside>'''


def faq_schema(faqs: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }


def faq_html(faqs: list[tuple[str, str]]) -> str:
    items = []
    for q, a in faqs:
        items.append(
            f'''<details class="faq-item">
  <summary>{esc(q)}</summary>
  <div class="faq-answer"><p>{esc(a)}</p></div>
</details>'''
        )
    return "\n".join(items)


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def org_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Locksmith",
        "name": BRAND,
        "url": DOMAIN + "/",
        "logo": DOMAIN + "/LOGO.png",
        "image": DOMAIN + "/assets/images/porsche-night.jpg",
        "telephone": PHONE_SCHEMA,
        "priceRange": "$$",
        "description": "24/7 mobile automotive locksmith specializing in vehicle lockouts, lost car keys, key fob programming, and emergency automotive locksmith services throughout Southwest Florida.",
        "areaServed": [a["name"] for a in AREAS] + ["Southwest Florida"],
        "serviceType": [s["name"] for s in SERVICES],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ],
            "opens": "00:00",
            "closes": "23:59",
        },
    }


def build_service_pages():
    # Services index
    cards = "\n".join(
        f'''<a class="service-tile" href="/services/{s["slug"]}/">
  <span class="service-tile-eyebrow">{esc(s["eyebrow"])}</span>
  <h2>{esc(s["name"])}</h2>
  <p>{esc(s["short"])}</p>
  <span class="service-tile-link">View service →</span>
</a>'''
        for s in SERVICES
    )
    crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Services", None)])
    html = f'''{head(
        f"Automotive Locksmith Services | {BRAND}",
        "Explore Lockout Pro SWFL automotive locksmith services: car lockouts, lost keys, key fob programming, ignition repair, and more across Southwest Florida.",
        f"{DOMAIN}/services/",
        og_image=f"{DOMAIN}/assets/images/hero-car.jpg",
        schemas=[org_schema(), crumb_schema],
    )}
<body class="inner-page">
{header("services")}
<section class="page-hero page-hero-services">
  <div class="page-hero-media" style="background-image:url('/assets/images/hero-car.jpg')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">AUTOMOTIVE ONLY</p>
    <h1>Automotive Locksmith Services</h1>
    <p class="page-hero-lead">Emergency lockouts, key replacement, fob programming, and ignition help — mobile across Southwest Florida.</p>
    <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  </div>
</section>
{crumb_nav}
<section class="section">
  <div class="container service-tile-grid">{cards}</div>
</section>
<section class="roadside-cta">
  <div class="container roadside-cta-inner">
    <div>
      <p class="eyebrow">LOCKED OUT RIGHT NOW?</p>
      <h2>We're On The Way.</h2>
      <p>Fast mobile automotive locksmith response across SWFL.</p>
    </div>
    <a class="btn btn-primary btn-xl" href="tel:{PHONE_TEL}">CALL NOW {PHONE_DISPLAY}</a>
  </div>
</section>
{footer()}
</body>
</html>'''
    write(ROOT / "services" / "index.html", html)

    for s in SERVICES:
        related = "".join(
            f'<li><a href="/services/{slug}/">{esc(SERVICE_BY_SLUG[slug]["name"])}</a></li>'
            for slug in s["related"]
            if slug in SERVICE_BY_SLUG
        )
        body_sections = "".join(
            f"<section class=\"content-block\"><h2>{esc(h)}</h2><p>{esc(p)}</p></section>"
            for h, p in s["body"]
        )
        area_links = ", ".join(
            f'<a href="/locations/{a["slug"]}/">{esc(a["name"])}</a>' for a in AREAS[:6]
        )
        crumb_nav, crumb_schema = breadcrumbs(
            [("Home", "/"), ("Services", "/services/"), (s["name"], None)]
        )
        service_schema = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": s["name"],
            "serviceType": s["name"],
            "description": s["meta_desc"],
            "url": f"{DOMAIN}/services/{s['slug']}/",
            "provider": {
                "@type": "Locksmith",
                "name": BRAND,
                "telephone": PHONE_SCHEMA,
                "url": DOMAIN + "/",
            },
            "areaServed": [a["name"] for a in AREAS],
        }
        html = f'''{head(
            s["meta_title"],
            s["meta_desc"],
            f"{DOMAIN}/services/{s['slug']}/",
            og_image=DOMAIN + s["image"],
            schemas=[service_schema, crumb_schema, faq_schema(s["faqs"])],
        )}
<body class="inner-page">
{header("services")}
<section class="page-hero">
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
        <p>Serving drivers in {area_links}, and surrounding Southwest Florida communities. Call <strong>{PHONE_DISPLAY}</strong> for fast mobile help.</p>
      </div>
      {body_sections}
      <section class="content-block">
        <h2>Related Services</h2>
        <ul class="text-list">{related}</ul>
      </section>
      <section class="content-block">
        <h2>Frequently Asked Questions</h2>
        <div class="faq-list">{faq_html(s["faqs"])}</div>
      </section>
    </div>
    {sidebar(s["slug"])}
  </div>
</section>
<section class="roadside-cta">
  <div class="container roadside-cta-inner">
    <div>
      <p class="eyebrow">NEED THIS SERVICE NOW?</p>
      <h2>Call Lockout Pro SWFL</h2>
      <p>Mobile automotive specialists · Damage-conscious methods · Clear communication</p>
    </div>
    <a class="btn btn-primary btn-xl" href="tel:{PHONE_TEL}">CALL {PHONE_DISPLAY}</a>
  </div>
</section>
{footer()}
</body>
</html>'''
        write(ROOT / "services" / s["slug"] / "index.html", html)


def build_location_pages():
    cards = "\n".join(
        f'''<a class="area-tile" href="/locations/{a["slug"]}/">
  <span class="area-tile-county">{esc(a["county"])}</span>
  <h2>{esc(a["name"])}</h2>
  <p>Emergency automotive locksmith service in {esc(a["name"])}.</p>
  <span class="service-tile-link">View area →</span>
</a>'''
        for a in AREAS
    )
    crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Service Areas", None)])
    html = f'''{head(
        f"Service Areas | Automotive Locksmith Across SWFL | {BRAND}",
        "Lockout Pro SWFL serves Fort Myers, Cape Coral, Naples, Bonita Springs, Estero, and more with 24/7 automotive locksmith service.",
        f"{DOMAIN}/locations/",
        schemas=[org_schema(), crumb_schema],
    )}
<body class="inner-page">
{header("locations")}
<section class="page-hero page-hero-areas">
  <div class="page-hero-media" style="background-image:url('/assets/images/driving.jpg')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">SOUTHWEST FLORIDA</p>
    <h1>Emergency Service Areas</h1>
    <p class="page-hero-lead">Mobile automotive locksmith coverage across Lee and Collier County communities.</p>
    <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  </div>
</section>
{crumb_nav}
<section class="section">
  <div class="container area-tile-grid">{cards}</div>
</section>
{footer()}
</body>
</html>'''
    write(ROOT / "locations" / "index.html", html)

    top_services = SERVICES[:8]
    for a in AREAS:
        service_links = "".join(
            f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])} in {esc(a["name"])}</a></li>'
            for s in top_services
        )
        other_areas = "".join(
            f'<li><a href="/locations/{o["slug"]}/">{esc(o["name"])}</a></li>'
            for o in AREAS
            if o["slug"] != a["slug"]
        )
        crumb_nav, crumb_schema = breadcrumbs(
            [("Home", "/"), ("Service Areas", "/locations/"), (a["name"], None)]
        )
        local_schema = {
            "@context": "https://schema.org",
            "@type": "Locksmith",
            "name": f"{BRAND} — {a['name']}",
            "url": f"{DOMAIN}/locations/{a['slug']}/",
            "telephone": PHONE_SCHEMA,
            "areaServed": a["name"],
            "description": f"24/7 automotive locksmith serving {a['name']}, {a['county']}, Florida — car lockouts, lost keys, key fob programming, and more.",
            "parentOrganization": {"@type": "Locksmith", "name": BRAND, "url": DOMAIN + "/"},
        }
        faqs = [
            (
                f"Do you provide car lockouts in {a['name']}?",
                f"Yes. Lockout Pro SWFL provides mobile car lockout service throughout {a['name']} and nearby {a['county']} communities.",
            ),
            (
                f"Can you replace lost car keys in {a['name']}?",
                f"In many cases yes. Call with your vehicle year, make, and model for {a['name']} mobile key replacement options.",
            ),
            (
                f"How fast can you reach {a['name']}?",
                "Arrival time depends on your exact location and current call volume. We'll give a realistic estimate when you call.",
            ),
            (
                "Are you automotive only?",
                "Yes. We focus exclusively on automotive locksmith services. For home or business locks, visit A Good Locksmith.",
            ),
        ]
        html = f'''{head(
            f"Automotive Locksmith in {a['name']} FL | {BRAND}",
            f"Need an automotive locksmith in {a['name']}? Lockout Pro SWFL offers 24/7 car lockouts, lost keys, and key fob programming. Call {PHONE_DISPLAY}.",
            f"{DOMAIN}/locations/{a['slug']}/",
            og_image=f"{DOMAIN}/assets/images/driving.jpg",
            schemas=[local_schema, crumb_schema, faq_schema(faqs)],
        )}
<body class="inner-page">
{header("locations")}
<section class="page-hero">
  <div class="page-hero-media" style="background-image:url('/assets/images/luxury-car.jpg')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">{esc(a["county"]).upper()} · FLORIDA</p>
    <h1>Automotive Locksmith in {esc(a["name"])}</h1>
    <p class="page-hero-lead">Fast mobile car lockouts, lost key replacement, and fob programming for {esc(a["name"])} drivers.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      <a class="btn btn-ghost" href="/services/car-lockouts/">Car Lockouts</a>
    </div>
  </div>
</section>
{crumb_nav}
<section class="section page-layout">
  <div class="container page-layout-grid">
    <div class="page-main">
      <div class="content-block intro-block">
        <p>When you're locked out in <strong>{esc(a["name"])}</strong>, you need a specialist who comes to you — fast. Lockout Pro SWFL is the mobile automotive locksmith focused exclusively on vehicle lockouts, keys, fobs, and ignition help throughout {esc(a["county"])}.</p>
        <p>Call <strong>{PHONE_DISPLAY}</strong> for emergency response in {esc(a["name"])}. Have your vehicle year, make, and model ready so we arrive prepared.</p>
      </div>
      <section class="content-block">
        <h2>Automotive Services in {esc(a["name"])}</h2>
        <ul class="text-list">{service_links}</ul>
      </section>
      <section class="content-block">
        <h2>Why Drivers in {esc(a["name"])} Call Us</h2>
        <p>We lead with emergency assistance — not generic locksmith messaging. Whether you're at a plaza, apartment complex, beach access, or driveway in {esc(a["name"])}, our process is built for clear communication and damage-conscious vehicle entry.</p>
        <ul class="check-list">
          <li>24/7 emergency automotive response</li>
          <li>Mobile service to your location</li>
          <li>Car lockouts, lost keys, and fob programming</li>
          <li>Local Southwest Florida coverage</li>
        </ul>
      </section>
      <section class="content-block">
        <h2>Nearby Areas</h2>
        <ul class="text-list">{other_areas}</ul>
      </section>
      <section class="content-block">
        <h2>{esc(a["name"])} FAQ</h2>
        <div class="faq-list">{faq_html(faqs)}</div>
      </section>
    </div>
    {sidebar()}
  </div>
</section>
<section class="roadside-cta">
  <div class="container roadside-cta-inner">
    <div>
      <p class="eyebrow">{esc(a["name"]).upper()} EMERGENCY</p>
      <h2>Locked Out in {esc(a["name"])}?</h2>
      <p>Call now for mobile automotive locksmith help.</p>
    </div>
    <a class="btn btn-primary btn-xl" href="tel:{PHONE_TEL}">CALL {PHONE_DISPLAY}</a>
  </div>
</section>
{footer()}
</body>
</html>'''
        write(ROOT / "locations" / a["slug"] / "index.html", html)


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
</a>'''
        for r in RESOURCES
    )
    crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Resource Center", None)])
    item_list = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Resource Center",
        "description": "Automotive locksmith guides from Lockout Pro SWFL.",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i,
                "item": {
                    "@type": "BlogPosting",
                    "headline": r["title"],
                    "url": f"{DOMAIN}/resources/{r['slug']}/",
                    "description": r["meta_desc"],
                    "author": {"@type": "Organization", "name": BRAND},
                },
            }
            for i, r in enumerate(RESOURCES, 1)
        ],
    }
    html = f'''{head(
        f"Resource Center | Automotive Locksmith Guides | {BRAND}",
        "Practical automotive locksmith guides for SWFL drivers: lockouts, lost keys, fob failures, ignition warning signs, and more.",
        f"{DOMAIN}/resources/",
        schemas=[item_list, crumb_schema],
    )}
<body class="inner-page">
{header("resources")}
<section class="page-hero">
  <div class="page-hero-media" style="background-image:url('/assets/images/key-fob.jpg')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">RESOURCE CENTER</p>
    <h1>Automotive Locksmith Guides</h1>
    <p class="page-hero-lead">Clear answers for lockouts, lost keys, fobs, and ignition problems — written for Southwest Florida drivers.</p>
  </div>
</section>
{crumb_nav}
<section class="section">
  <div class="container resource-grid">{cards}</div>
</section>
{footer()}
</body>
</html>'''
    write(ROOT / "resources" / "index.html", html)

    for r in RESOURCES:
        sections = "".join(
            f"<section class=\"content-block\"><h2>{esc(h)}</h2><p>{esc(p)}</p></section>"
            for h, p in r["sections"]
        )
        others = "".join(
            f'<li><a href="/resources/{o["slug"]}/">{esc(o["title"])}</a></li>'
            for o in RESOURCES
            if o["slug"] != r["slug"]
        )
        crumb_nav, crumb_schema = breadcrumbs(
            [("Home", "/"), ("Resources", "/resources/"), (r["title"], None)]
        )
        article_schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": r["title"],
            "description": r["meta_desc"],
            "image": DOMAIN + r["image"],
            "datePublished": "2026-08-07",
            "dateModified": TODAY,
            "author": {"@type": "Organization", "name": BRAND},
            "publisher": {
                "@type": "Organization",
                "name": BRAND,
                "logo": {"@type": "ImageObject", "url": DOMAIN + "/LOGO.png"},
            },
            "mainEntityOfPage": f"{DOMAIN}/resources/{r['slug']}/",
        }
        html = f'''{head(
            f"{r['title']} | {BRAND}",
            r["meta_desc"],
            f"{DOMAIN}/resources/{r['slug']}/",
            og_image=DOMAIN + r["image"],
            schemas=[article_schema, crumb_schema, faq_schema(r["faqs"])],
            article=True,
        )}
<body class="inner-page">
{header("resources")}
<section class="page-hero article-hero">
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
    <article class="page-main article-main">
      <div class="content-block intro-block">
        <p>{esc(r["intro"])}</p>
        <p>Need help now? Call <a href="tel:{PHONE_TEL}"><strong>{PHONE_DISPLAY}</strong></a> for mobile automotive locksmith service across Southwest Florida.</p>
      </div>
      {sections}
      <section class="content-block">
        <h2>Related Guides</h2>
        <ul class="text-list">{others}</ul>
      </section>
      <section class="content-block">
        <h2>FAQ</h2>
        <div class="faq-list">{faq_html(r["faqs"])}</div>
      </section>
    </article>
    {sidebar()}
  </div>
</section>
<section class="roadside-cta">
  <div class="container roadside-cta-inner">
    <div>
      <p class="eyebrow">STILL STUCK?</p>
      <h2>Talk To An Automotive Specialist</h2>
    </div>
    <a class="btn btn-primary btn-xl" href="tel:{PHONE_TEL}">CALL {PHONE_DISPLAY}</a>
  </div>
</section>
{footer()}
</body>
</html>'''
        write(ROOT / "resources" / r["slug"] / "index.html", html)


def build_sitemap_and_llms():
    urls = [
        (f"{DOMAIN}/", "1.0", "weekly"),
        (f"{DOMAIN}/services/", "0.9", "weekly"),
        (f"{DOMAIN}/locations/", "0.9", "weekly"),
        (f"{DOMAIN}/resources/", "0.9", "weekly"),
    ]
    for s in SERVICES:
        urls.append((f"{DOMAIN}/services/{s['slug']}/", "0.8", "monthly"))
    for a in AREAS:
        urls.append((f"{DOMAIN}/locations/{a['slug']}/", "0.8", "monthly"))
    for r in RESOURCES:
        urls.append((f"{DOMAIN}/resources/{r['slug']}/", "0.7", "monthly"))

    body = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, pri, freq in urls:
        body.append(
            f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>"""
        )
    body.append("</urlset>")
    write(ROOT / "sitemap.xml", "\n".join(body) + "\n")

    write(
        ROOT / "robots.txt",
        f"""User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
""",
    )

    service_lines = "\n".join(
        f"- {s['name']}: {DOMAIN}/services/{s['slug']}/" for s in SERVICES
    )
    city_lines = "\n".join(
        f"- {a['name']}: {DOMAIN}/locations/{a['slug']}/" for a in AREAS
    )
    article_lines = "\n".join(
        f"- {r['title']}: {DOMAIN}/resources/{r['slug']}/" for r in RESOURCES
    )
    write(
        ROOT / "llms.txt",
        f"""# {BRAND}

Website:
{DOMAIN}/

Business:
{BRAND}

Description:
Mobile automotive locksmith serving Southwest Florida. Emergency car lockouts, lost car keys, key fob programming, smart keys, ignition assistance, and related automotive locksmith services.

Phone:
{PHONE_DISPLAY}

Business Type:
Mobile Automotive Locksmith (automotive only)

Primary Service Area:
Fort Myers
Cape Coral
Naples
Bonita Springs
Estero
North Naples
Fort Myers Beach
Lehigh Acres
San Carlos Park
North Fort Myers
Southwest Florida

Services:
{service_lines}

City Pages:
{city_lines}

Resource Center:
{DOMAIN}/resources/

Articles:
{article_lines}

Sister Company:
A Good Locksmith (residential & commercial): https://agoodlocksmith.com

Website Purpose:
Help stranded drivers in Southwest Florida quickly reach a professional automotive locksmith and understand vehicle key and lockout options.
""",
    )


def main():
    build_service_pages()
    build_location_pages()
    build_resource_pages()
    build_sitemap_and_llms()
    print("Inner pages generated.")


if __name__ == "__main__":
    main()
