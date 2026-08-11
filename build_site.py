#!/usr/bin/env python3
"""Generate Lockout Pro SWFL — automotive LOCKOUT specialist site."""

from pathlib import Path
from datetime import date
import json
import shutil

ROOT = Path(__file__).resolve().parent
DOMAIN = "https://lockoutproswfl.com"
PHONE_DISPLAY = "(239) 380-5240"
PHONE_TEL = "2393805240"
PHONE_SCHEMA = "+1-239-380-5240"
BRAND = "Lockout Pro SWFL"
TODAY = date.today().isoformat()
AGL = "https://agoodlocksmith.com"

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
        "short": "Keys locked inside? We unlock cars, trucks, and SUVs across Southwest Florida.",
        "eyebrow": "PRIMARY SERVICE",
        "h1": "Car Lockout Service in Southwest Florida",
        "meta_title": "Car Lockouts SWFL | 24/7 Vehicle Unlock Service | Lockout Pro",
        "meta_desc": "Locked out of your car in Fort Myers, Cape Coral, Naples or SWFL? Lockout Pro specializes in fast car lockout service. Call (239) 380-5240.",
        "intro": "Keys on the seat. Door locked. Heat climbing. A car lockout is exactly what Lockout Pro SWFL is built for — getting you back into your vehicle without turning a bad moment into vehicle damage.",
        "body": [
            ("Locked Out? We're On The Way", "Lockout Pro focuses on automotive lockouts. When your keys are inside the car, truck, or SUV, call us. We come to your location across Southwest Florida with professional entry tools designed for modern vehicles."),
            ("What To Tell Us When You Call", "Share your exact location and your vehicle year, make, and model. If a child or pet is inside, or the engine is running, tell us immediately so we can prioritize accordingly."),
            ("Damage-Conscious Entry", "Improvised tools and viral unlock hacks commonly damage weather seals, paint, wiring, or linkages. Professional automotive lockout methods are built to open the door carefully."),
        ],
        "faqs": [
            ("How fast can you unlock my car?", "Arrival time depends on your location and current calls. When you call, we give a realistic estimate for your area."),
            ("Will unlocking damage my door?", "We use professional automotive entry methods intended to minimize risk. DIY tools are far more likely to cause damage."),
            ("Do you unlock cars in Naples and Cape Coral?", "Yes. We cover Fort Myers, Cape Coral, Naples, Estero, Bonita Springs, Lehigh Acres, and surrounding Southwest Florida communities."),
            ("What if my keys are lost, not locked inside?", "Lockout Pro specializes in lockouts. For key replacement and programming, our related company A Good Locksmith can help."),
        ],
        "related": ["emergency-vehicle-lockout", "trunk-lockouts", "fleet-vehicle-lockouts"],
        "image": "/assets/images/hero-collage.jpg",
    },
    {
        "slug": "emergency-vehicle-lockout",
        "name": "Emergency Vehicle Lockout",
        "short": "24/7 emergency response when you're locked out of your vehicle.",
        "eyebrow": "24/7 EMERGENCY",
        "h1": "Emergency Vehicle Lockout Service",
        "meta_title": "Emergency Vehicle Lockout SWFL | 24/7 | Lockout Pro",
        "meta_desc": "Emergency vehicle lockout help in Southwest Florida. Locked out day or night? Call Lockout Pro at (239) 380-5240.",
        "intro": "Lockouts don't wait for business hours. Lockout Pro SWFL provides emergency vehicle lockout service across Southwest Florida when you need help now.",
        "body": [
            ("Built For Urgent Lockouts", "Whether you're locked out after dark, at work, at the store, or on the roadside, our focus is clear: get you back into your vehicle."),
            ("When It's An Emergency", "Call immediately if someone is locked inside, the engine is running with kids or pets in the car, you're in an unsafe area, or you're stranded in extreme heat."),
            ("Clear Communication", "When you call, we confirm your location, vehicle details, and a realistic arrival window — so you're not left guessing."),
        ],
        "faqs": [
            ("Are you available 24/7 for lockouts?", "Yes. Emergency vehicle lockout service is available around the clock across our SWFL coverage area."),
            ("What should I do while I wait?", "Stay near the vehicle in a safe place. Avoid forcing the door with household tools. See our locked-out guide for practical tips."),
            ("Do you only do lockouts?", "Yes — Lockout Pro is the automotive lockout specialist. For key replacement, programming, or home/business locks, visit A Good Locksmith."),
            ("What areas do you cover after hours?", "Fort Myers, Cape Coral, Naples, Estero, Bonita Springs, and surrounding Southwest Florida communities."),
        ],
        "related": ["car-lockouts", "trunk-lockouts", "commercial-vehicle-lockout"],
        "image": "/assets/images/swfl-vehicles.jpg",
    },
    {
        "slug": "trunk-lockouts",
        "name": "Trunk Lockouts",
        "short": "Keys locked in the trunk? We help you regain access carefully.",
        "eyebrow": "TRUNK ACCESS",
        "h1": "Trunk Lockout Service",
        "meta_title": "Trunk Lockouts SWFL | Keys Locked In Trunk | Lockout Pro",
        "meta_desc": "Keys locked in the trunk in Fort Myers or SWFL? Lockout Pro provides professional trunk lockout help. Call (239) 380-5240.",
        "intro": "Keys in the trunk and no easy way back in — that's a lockout problem Lockout Pro handles. We use vehicle-appropriate methods, not crowbars.",
        "body": [
            ("Cabin First Or Trunk Direct", "Some vehicles allow cabin entry that restores trunk release. Others need a trunk-focused approach. We choose the method that fits your vehicle."),
            ("Protect Latches And Seals", "Forced entry can destroy trunk latches and weather seals. Professional lockout methods prioritize controlled access."),
            ("Common Situations", "Grocery runs, beach days, and parking lots across Southwest Florida are frequent trunk-lockout scenes."),
        ],
        "faqs": [
            ("Can you open a trunk without keys?", "In many cases yes, using vehicle-appropriate lockout techniques."),
            ("My keys are in the trunk and the car is locked — can you help?", "Yes. That's a common emergency call for Lockout Pro."),
            ("Will you damage the trunk?", "Our goal is careful, non-destructive access whenever possible."),
            ("What if only the electronic trunk release failed?", "Tell us the symptoms when you call so we can prepare the right approach."),
        ],
        "related": ["car-lockouts", "emergency-vehicle-lockout", "fleet-vehicle-lockouts"],
        "image": "/assets/images/swfl-vehicles.jpg",
    },
    {
        "slug": "fleet-vehicle-lockouts",
        "name": "Fleet Vehicle Lockouts",
        "short": "Lockout response for work trucks, vans, and company vehicles.",
        "eyebrow": "FLEET LOCKOUTS",
        "h1": "Fleet Vehicle Lockout Service",
        "meta_title": "Fleet Vehicle Lockouts SWFL | Work Truck Unlock | Lockout Pro",
        "meta_desc": "Fleet vehicle locked out in SWFL? Lockout Pro helps businesses with work truck, van, and company vehicle lockouts. Call (239) 380-5240.",
        "intro": "A locked work vehicle stops a job. Lockout Pro SWFL helps Southwest Florida businesses get fleet vehicles open again — quickly and without unnecessary complication.",
        "body": [
            ("Downtime Matters", "When a truck, van, or company car is locked with keys inside, we focus on practical turnaround so your team can get back to work."),
            ("What Fleets Call Us For", "Keys locked in cabins, trunks, and job-site vehicles across Fort Myers, Cape Coral, Naples, and nearby communities."),
            ("One Call Coordination", "Share the vehicle details and location — we'll coordinate mobile lockout service across our coverage area."),
        ],
        "faqs": [
            ("Do you help small business fleets?", "Yes — from a few vehicles to larger local fleets needing lockout help."),
            ("Can you unlock work trucks and vans?", "In many cases yes. Call with year, make, and model."),
            ("What if we need spare keys for the fleet?", "Lockout Pro focuses on lockouts. For key and fob needs, ask about A Good Locksmith."),
            ("Do you come to job sites?", "Yes — mobile lockout service to your location across SWFL."),
        ],
        "related": ["commercial-vehicle-lockout", "car-lockouts", "emergency-vehicle-lockout"],
        "image": "/assets/images/driving.jpg",
    },
    {
        "slug": "commercial-vehicle-lockout",
        "name": "Commercial Vehicle Lockout",
        "short": "Lockout help for commercial vehicles stranded with keys inside.",
        "eyebrow": "COMMERCIAL",
        "h1": "Commercial Vehicle Lockout Service",
        "meta_title": "Commercial Vehicle Lockout SWFL | Lockout Pro",
        "meta_desc": "Commercial vehicle lockout service in Southwest Florida. Locked out of a work or commercial vehicle? Call Lockout Pro at (239) 380-5240.",
        "intro": "Commercial vehicles lock out the same way daily drivers do — and the cost of waiting is often higher. Lockout Pro SWFL provides focused lockout response for commercial vehicles across Southwest Florida.",
        "body": [
            ("Business Lockouts, Handled Simply", "Call with your location and vehicle details. We come to you and focus on getting the vehicle open."),
            ("Parking Lots, Job Sites, And Depots", "Wherever the commercial vehicle is stranded in our service area, mobile lockout help is the point."),
            ("Related Needs", "If your situation involves key replacement rather than a lockout, we'll point you to the right help through A Good Locksmith."),
        ],
        "faqs": [
            ("Is a commercial lockout different from a car lockout?", "The goal is the same — careful vehicle entry. Vehicle type and location details help us prepare."),
            ("Can you unlock box trucks or vans?", "Often yes depending on the vehicle. Call with details."),
            ("Do you invoice businesses?", "Call to discuss your needs and service process."),
            ("What if keys are lost rather than locked inside?", "That's typically a key service — A Good Locksmith handles broader automotive key needs."),
        ],
        "related": ["fleet-vehicle-lockouts", "car-lockouts", "emergency-vehicle-lockout"],
        "image": "/assets/images/driving.jpg",
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

# Old service URLs → redirect targets (keep SEO equity / avoid dead links)
SERVICE_REDIRECTS = {
    "lost-car-keys": ("/services/car-lockouts/", "Lost key situations often start as emergencies. Lockout Pro specializes in vehicle lockouts — if your keys are locked inside, call us. For key replacement, see A Good Locksmith."),
    "car-key-replacement": (AGL + "/services/car-key-replacement/", "Lockout Pro specializes in automotive lockouts. For car key replacement, visit A Good Locksmith."),
    "key-fob-programming": (AGL + "/services/key-programming/", "Lockout Pro specializes in automotive lockouts. For key fob programming, visit A Good Locksmith."),
    "smart-keys": (AGL + "/services/automotive-locksmith/", "Lockout Pro specializes in automotive lockouts. For smart key help, visit A Good Locksmith."),
    "push-to-start-keys": (AGL + "/services/automotive-locksmith/", "Lockout Pro specializes in automotive lockouts. For push-to-start key help, visit A Good Locksmith."),
    "broken-car-key-extraction": (AGL + "/services/automotive-locksmith/", "Lockout Pro specializes in automotive lockouts. For broken key extraction, visit A Good Locksmith."),
    "ignition-repair": (AGL + "/services/automotive-locksmith/", "Lockout Pro specializes in automotive lockouts. For ignition help, visit A Good Locksmith."),
    "duplicate-car-keys": (AGL + "/services/car-key-replacement/", "Lockout Pro specializes in automotive lockouts. For spare/duplicate keys, visit A Good Locksmith."),
    "motorcycle-keys": (AGL + "/services/automotive-locksmith/", "Lockout Pro specializes in automotive lockouts. For motorcycle keys, visit A Good Locksmith."),
    "emergency-automotive-locksmith": ("/services/emergency-vehicle-lockout/", "This page has moved to our Emergency Vehicle Lockout service."),
    "fleet-vehicle-locksmith": ("/services/fleet-vehicle-lockouts/", "This page has moved to Fleet Vehicle Lockouts."),
}

RESOURCES = [
    {
        "slug": "locked-out-of-your-car",
        "title": "Locked Out Of Your Car? Here's What To Do",
        "eyebrow": "EMERGENCY GUIDE",
        "meta_desc": "Locked your keys in the car in SWFL? Stay safe, avoid damage, and get professional lockout help fast.",
        "minutes": 5,
        "image": "/assets/images/hero-collage.jpg",
        "intro": "A car lockout rarely happens at a convenient time. The next few minutes matter — the wrong DIY move can damage seals, paint, or linkages. Here's what to do.",
        "sections": [
            ("1. Check Safety First", "If a child or pet is inside, call for help immediately and tell the locksmith. Move to a safe place near the vehicle. In heat, prioritize shade and hydration while you wait."),
            ("2. Confirm It's Actually Locked", "Try every door. Check for a spare. Ask if anyone nearby has a second fob. Don't force anything."),
            ("3. Avoid DIY Entry Tools", "Coat hangers, knives, and viral unlock hacks commonly damage weatherstripping, wiring, paint, and airbag components."),
            ("4. Call A Vehicle Lockout Specialist", "Provide your exact location and vehicle year/make/model. Lockout Pro SWFL specializes in automotive lockouts across Southwest Florida."),
            ("5. After You're Back In", "Consider keeping a properly stored spare key strategy so the next lockout is less likely — and never hide a key on the vehicle in an obvious spot."),
        ],
        "faqs": [
            ("Can a locksmith unlock my car without damaging it?", "In most lockout situations, yes. Professionals use vehicle-appropriate tools and aim for careful entry."),
            ("What if my keys are lost, not locked inside?", "That's usually a key replacement situation. Lockout Pro focuses on lockouts; A Good Locksmith can help with keys."),
            ("Should I try to unlock the car myself?", "If everyone is safe, avoid improvised tools. DIY methods commonly cause expensive damage."),
        ],
    },
    {
        "slug": "prevent-locking-keys-in-your-car",
        "title": "How To Prevent Locking Keys In Your Car",
        "eyebrow": "PREVENTION",
        "meta_desc": "Practical habits to stop locking your keys in the car — simple tips for Southwest Florida drivers.",
        "minutes": 4,
        "image": "/assets/images/swfl-vehicles.jpg",
        "intro": "Most lockouts are preventable. A few habits dramatically reduce the odds you'll be standing in a hot parking lot waiting for help.",
        "sections": [
            ("Keep The Fob In A Fixed Place", "Same pocket or bag pocket every time — especially during grocery runs, beach days, and school pickup."),
            ("Learn Your Auto-Lock Behavior", "Some vehicles lock automatically. Know your model's behavior so it doesn't lock behind you with keys inside."),
            ("Have A Spare Strategy", "A working spare kept separately from your daily key is the simplest lockout prevention."),
            ("Watch Soft-Close Doors", "Distraction plus soft-close doors is a classic lockout recipe. Pause before walking away."),
            ("Phone Apps Aren't Enough", "Manufacturer apps can help on some newer cars, but connectivity fails. Don't treat an app as your only backup."),
        ],
        "faqs": [
            ("What's the #1 lockout prevention tip?", "Own a working spare key stored separately from your daily key."),
            ("Do auto-lock features cause lockouts?", "They can, especially when drivers are unfamiliar with a vehicle."),
            ("Should I hide a key on the car?", "Magnetic hide-a-keys are risky. A secure spare at home is safer."),
        ],
    },
    {
        "slug": "how-much-does-a-car-lockout-cost",
        "title": "How Much Does A Car Lockout Cost?",
        "eyebrow": "PRICING GUIDE",
        "meta_desc": "What affects car lockout pricing in SWFL? Learn the factors behind vehicle unlock service costs.",
        "minutes": 4,
        "image": "/assets/images/automotive-work.jpg",
        "intro": "Car lockout pricing isn't one flat number — vehicle type, location, time of day, and complexity all matter. Here's what Southwest Florida drivers should know.",
        "sections": [
            ("Vehicle Details Matter", "Modern vehicles have different lock designs and security systems. Year, make, and model help a lockout specialist prepare — and quote more accurately."),
            ("Location And Timing", "After-hours emergencies and farther locations can affect response. Clear communication when you call helps set expectations."),
            ("Complexity Of The Lockout", "A straightforward cabin lockout differs from certain trunk situations or vehicles with unique entry considerations."),
            ("Beware Of Too-Good Quotes", "Be wary of prices that sound impossibly low without asking for vehicle details. Provide accurate information and ask for a clear estimate."),
            ("The Cost Of DIY Damage", "A cheap pry attempt that breaks a seal or linkage often costs more than calling a professional lockout service."),
        ],
        "faqs": [
            ("Why won't anyone give an exact price by text?", "Because vehicles vary. Accurate estimates need year, make, model, and lockout details."),
            ("Is the cheapest quote the best deal?", "Not if it leads to damage or bait-and-switch pricing."),
            ("Does Lockout Pro replace keys too?", "Lockout Pro specializes in lockouts. For key replacement and programming, see A Good Locksmith."),
        ],
    },
    {
        "slug": "locked-out-engine-running",
        "title": "Locked Out With The Engine Running?",
        "eyebrow": "URGENT LOCKOUT",
        "meta_desc": "Locked out of a running car in SWFL? What to do next and when to call Lockout Pro immediately.",
        "minutes": 3,
        "image": "/assets/images/hero-collage.jpg",
        "intro": "A running vehicle with keys inside raises the stakes — heat, safety, and the risk of the car being left unattended. Stay calm and call for professional lockout help.",
        "sections": [
            ("Call Immediately", "Tell the lockout specialist the engine is running and share your exact location plus vehicle details."),
            ("Stay With The Vehicle If Safe", "Don't leave a running vehicle unattended if you can safely remain nearby."),
            ("Kids Or Pets Inside", "Say so immediately when you call so responders can prioritize."),
            ("Don't Smash A Window First", "Window breakage is a last resort and creates injury and cost risk. Professional entry is usually the better first call."),
            ("After You're Back In", "Once secure, consider how the lockout happened and put a spare-key plan in place."),
        ],
        "faqs": [
            ("Is a running-car lockout more urgent?", "Yes — especially with occupants inside or in extreme heat."),
            ("Can you unlock a car while it's running?", "In many cases yes. Tell us the situation when you call."),
            ("Should I call 911?", "If someone is in immediate danger, call emergency services first, then call for lockout help."),
        ],
    },
]

RESOURCE_REDIRECTS = {
    "lost-car-keys-guide": ("/resources/locked-out-of-your-car/", "Looking for lockout help? Start here. For key replacement, visit A Good Locksmith."),
    "how-much-does-a-car-locksmith-cost": ("/resources/how-much-does-a-car-lockout-cost/", "Updated guide focused on car lockout pricing."),
    "key-fob-stopped-working": (AGL + "/", "Lockout Pro specializes in lockouts. For key fob issues, visit A Good Locksmith."),
    "can-a-locksmith-replace-push-to-start-keys": (AGL + "/", "Lockout Pro specializes in lockouts. For push-to-start keys, visit A Good Locksmith."),
    "signs-ignition-cylinder-failing": (AGL + "/", "Lockout Pro specializes in lockouts. For ignition issues, visit A Good Locksmith."),
    "spare-car-keys-every-driver": (AGL + "/services/car-key-replacement/", "For spare car keys, visit A Good Locksmith. For lockouts, call Lockout Pro."),
}


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


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
      <img src="/LOGO.png" alt="{BRAND}" class="brand-logo" width="64" height="64">
      <span class="brand-text">
        <span class="brand-name"><span class="brand-lockout">LOCKOUT</span> <span class="brand-pro">PRO</span> <span class="brand-swfl">SWFL</span></span>
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
    <a href="/resources/">Resources</a>
    <a href="/#faq">FAQ</a>
    <a href="/#contact">Contact</a>
    <a class="mobile-call" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  </div>
</header>'''


def footer() -> str:
    service_links = "\n".join(
        f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SERVICES
    )
    area_links = "\n".join(
        f'<li><a href="/locations/{a["slug"]}/">{esc(a["name"])}</a></li>' for a in AREAS[:6]
    )
    return f'''<footer class="site-footer" id="contact">
  <div class="container footer-grid">
    <div class="footer-brand">
      <a class="brand footer-brand-link" href="/">
        <img src="/LOGO.png" alt="{BRAND}" width="56" height="56">
        <span class="brand-name"><span class="brand-lockout">LOCKOUT</span> <span class="brand-pro">PRO</span> <span class="brand-swfl">SWFL</span></span>
      </a>
      <p>Southwest Florida's automotive lockout specialist. Locked out of your vehicle? Call us.</p>
      <a class="footer-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <p class="footer-hours">Available 24/7 · Vehicle Lockouts</p>
    </div>
    <div>
      <h3>Lockout Services</h3>
      <ul>{service_links}</ul>
    </div>
    <div>
      <h3>Service Areas</h3>
      <ul>{area_links}
        <li><a href="/locations/">All Areas →</a></li>
      </ul>
    </div>
    <div>
      <h3>Need Keys Or Home Locks?</h3>
      <p>For key replacement, fobs, ignition work, or residential/commercial locksmith service:</p>
      <a class="footer-outlink" href="{AGL}" rel="noopener noreferrer" target="_blank">Visit A Good Locksmith →</a>
      <h3 class="footer-spaced">Resources</h3>
      <ul>
        <li><a href="/resources/">Resource Center</a></li>
        <li><a href="/resources/locked-out-of-your-car/">Locked Out Guide</a></li>
        <li><a href="/resources/how-much-does-a-car-lockout-cost/">Lockout Pricing</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <p>© {date.today().year} {BRAND}. All rights reserved.</p>
      <p>Automotive lockouts · Southwest Florida</p>
    </div>
  </div>
</footer>
<a href="tel:{PHONE_TEL}" class="sticky-call" aria-label="Call {BRAND} now">
  <span class="sticky-call-kicker">Locked Out?</span>
  <span class="sticky-call-num">CALL {PHONE_DISPLAY}</span>
</a>
<script src="/script.js" defer></script>'''


def head(title, description, canonical, og_image=f"{DOMAIN}/assets/images/hero-collage.jpg", schemas=None, article=False):
    schema_html = ""
    if schemas:
        for schema in schemas:
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
    lis = []
    schema_items = []
    for i, (name, href) in enumerate(items, 1):
        if href:
            lis.append(f'<li><a href="{href}">{esc(name)}</a></li>')
            schema_items.append({"@type": "ListItem", "position": i, "name": name, "item": DOMAIN + href if href.startswith("/") else href})
        else:
            lis.append(f'<li aria-current="page"><span>{esc(name)}</span></li>')
            schema_items.append({"@type": "ListItem", "position": i, "name": name})
    nav = f'''<div class="container breadcrumb-wrap">
<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>
</div>'''
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": schema_items}
    return nav, schema


def sidebar(current_service=None):
    links = "\n".join(
        '<li><a href="/services/{slug}/"{cls}>{name}</a></li>'.format(
            slug=s["slug"],
            cls=' class="current"' if current_service == s["slug"] else "",
            name=esc(s["name"]),
        )
        for s in SERVICES
    )
    areas = "\n".join(
        f'<li><a href="/locations/{a["slug"]}/">{esc(a["name"])}</a></li>' for a in AREAS[:8]
    )
    return f'''<aside class="page-sidebar">
  <div class="sidebar-card sidebar-cta">
    <p class="sidebar-kicker">Locked Out?</p>
    <a class="sidebar-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
    <a class="btn btn-primary btn-block" href="tel:{PHONE_TEL}">Call Now</a>
    <p class="sidebar-note">24/7 vehicle lockout service</p>
  </div>
  <div class="sidebar-card">
    <h3>Lockout Services</h3>
    <ul class="sidebar-links">{links}</ul>
  </div>
  <div class="sidebar-card">
    <h3>Areas</h3>
    <ul class="sidebar-links">{areas}</ul>
  </div>
</aside>'''


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def faq_html(faqs):
    return "\n".join(
        f'''<details class="faq-item">
  <summary>{esc(q)}</summary>
  <div class="faq-answer"><p>{esc(a)}</p></div>
</details>'''
        for q, a in faqs
    )


def org_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Locksmith",
        "name": BRAND,
        "url": DOMAIN + "/",
        "logo": DOMAIN + "/LOGO.png",
        "image": DOMAIN + "/assets/images/hero-collage.jpg",
        "telephone": PHONE_SCHEMA,
        "priceRange": "$$",
        "description": "24/7 automotive lockout specialist serving Southwest Florida. Car lockouts, emergency vehicle lockouts, trunk lockouts, and fleet lockout service.",
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
    return f'''{head(title, message, canonical, schemas=None)}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("services")}
<section class="page-hero" id="main">
  <div class="page-hero-media" style="background-image:url('/assets/images/hero-collage.jpg')"></div>
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
<section class="section">
  <div class="container" style="max-width:720px">
    <div class="content-block">
      <p>Lockout Pro SWFL is Southwest Florida's automotive <strong>lockout</strong> specialist. If your keys are locked inside your vehicle, call <a href="tel:{PHONE_TEL}"><strong>{PHONE_DISPLAY}</strong></a>.</p>
      <p style="margin-top:1rem"><a class="btn btn-primary" href="{target}"{" rel=\"noopener noreferrer\" target=\"_blank\"" if external else ""}>Go to the right page</a></p>
    </div>
  </div>
</section>
{footer()}
</body>
</html>'''


def build_service_pages():
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
        f"Vehicle Lockout Services | {BRAND}",
        "Lockout Pro SWFL lockout services: car lockouts, emergency vehicle lockouts, trunk lockouts, fleet and commercial vehicle lockouts across Southwest Florida.",
        f"{DOMAIN}/services/",
        schemas=[org_schema(), crumb_schema],
    )}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("services")}
<section class="page-hero page-hero-services" id="main">
  <div class="page-hero-media" style="background-image:url('/assets/images/hero-collage.jpg')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">AUTOMOTIVE LOCKOUTS</p>
    <h1>Vehicle Lockout Services</h1>
    <p class="page-hero-lead">One specialty: getting you back into your vehicle across Southwest Florida.</p>
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
      <h2>Call Lockout Pro SWFL</h2>
      <p>Vehicle lockout specialists serving Southwest Florida.</p>
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
            for slug in s["related"] if slug in SERVICE_BY_SLUG
        )
        body_sections = "".join(
            f'<section class="content-block"><h2>{esc(h)}</h2><p>{esc(p)}</p></section>'
            for h, p in s["body"]
        )
        area_links = ", ".join(
            f'<a href="/locations/{a["slug"]}/">{esc(a["name"])}</a>' for a in AREAS[:6]
        )
        crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Services", "/services/"), (s["name"], None)])
        service_schema = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": s["name"],
            "serviceType": s["name"],
            "description": s["meta_desc"],
            "url": f"{DOMAIN}/services/{s['slug']}/",
            "provider": {"@type": "Locksmith", "name": BRAND, "telephone": PHONE_SCHEMA, "url": DOMAIN + "/"},
            "areaServed": [a["name"] for a in AREAS],
        }
        html = f'''{head(s["meta_title"], s["meta_desc"], f"{DOMAIN}/services/{s['slug']}/", og_image=DOMAIN + s["image"], schemas=[service_schema, crumb_schema, faq_schema(s["faqs"])])}
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
      <a class="btn btn-ghost" href="/services/">All Lockout Services</a>
    </div>
  </div>
</section>
{crumb_nav}
<section class="section page-layout">
  <div class="container page-layout-grid">
    <div class="page-main">
      <div class="content-block intro-block">
        <p>{esc(s["intro"])}</p>
        <p>Serving drivers in {area_links}, and surrounding communities. Call <strong>{PHONE_DISPLAY}</strong>.</p>
      </div>
      {body_sections}
      <section class="content-block">
        <h2>Related Lockout Services</h2>
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
    </div>
    <a class="btn btn-primary btn-xl" href="tel:{PHONE_TEL}">CALL {PHONE_DISPLAY}</a>
  </div>
</section>
{footer()}
</body>
</html>'''
        write(ROOT / "services" / s["slug"] / "index.html", html)

    for old_slug, (target, msg) in SERVICE_REDIRECTS.items():
        title = old_slug.replace("-", " ").title()
        write(
            ROOT / "services" / old_slug / "index.html",
            redirect_page(title, msg, target, f"{DOMAIN}/services/{old_slug}/"),
        )


def build_location_pages():
    cards = "\n".join(
        f'''<a class="area-tile" href="/locations/{a["slug"]}/">
  <span class="area-tile-county">{esc(a["county"])}</span>
  <h2>{esc(a["name"])}</h2>
  <p>Vehicle lockout service in {esc(a["name"])}.</p>
  <span class="service-tile-link">View area →</span>
</a>'''
        for a in AREAS
    )
    crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Service Areas", None)])
    html = f'''{head(
        f"Service Areas | Vehicle Lockouts Across SWFL | {BRAND}",
        "Lockout Pro SWFL serves Fort Myers, Cape Coral, Naples, Bonita Springs, Estero, and more with 24/7 vehicle lockout service.",
        f"{DOMAIN}/locations/",
        schemas=[org_schema(), crumb_schema],
    )}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("locations")}
<section class="page-hero page-hero-areas" id="main">
  <div class="page-hero-media" style="background-image:url('/assets/images/swfl-vehicles.jpg')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">SOUTHWEST FLORIDA</p>
    <h1>Lockout Service Areas</h1>
    <p class="page-hero-lead">Mobile vehicle lockout coverage across Lee and Collier County communities.</p>
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

    for a in AREAS:
        service_links = "".join(
            f'<li><a href="/services/{s["slug"]}/">{esc(s["name"])} in {esc(a["name"])}</a></li>'
            for s in SERVICES
        )
        other_areas = "".join(
            f'<li><a href="/locations/{o["slug"]}/">{esc(o["name"])}</a></li>'
            for o in AREAS if o["slug"] != a["slug"]
        )
        crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Service Areas", "/locations/"), (a["name"], None)])
        local_schema = {
            "@context": "https://schema.org",
            "@type": "Locksmith",
            "name": f"{BRAND} — {a['name']}",
            "url": f"{DOMAIN}/locations/{a['slug']}/",
            "telephone": PHONE_SCHEMA,
            "areaServed": a["name"],
            "description": f"24/7 vehicle lockout service in {a['name']}, {a['county']}, Florida.",
            "parentOrganization": {"@type": "Locksmith", "name": BRAND, "url": DOMAIN + "/"},
        }
        faqs = [
            (f"Do you provide car lockouts in {a['name']}?", f"Yes. Lockout Pro SWFL provides mobile car lockout service throughout {a['name']} and nearby {a['county']} communities."),
            (f"How fast can you reach {a['name']}?", "Arrival time depends on your exact location and current call volume. We'll give a realistic estimate when you call."),
            ("Do you replace car keys too?", "Lockout Pro specializes in lockouts. For key replacement and programming, visit A Good Locksmith."),
            ("Are you available 24/7?", "Yes — emergency vehicle lockout service around the clock across our SWFL area."),
        ]
        html = f'''{head(
            f"Car Lockouts in {a['name']} FL | {BRAND}",
            f"Locked out in {a['name']}? Lockout Pro SWFL provides 24/7 vehicle lockout service. Call {PHONE_DISPLAY}.",
            f"{DOMAIN}/locations/{a['slug']}/",
            schemas=[local_schema, crumb_schema, faq_schema(faqs)],
        )}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("locations")}
<section class="page-hero" id="main">
  <div class="page-hero-media" style="background-image:url('/assets/images/hero-collage.jpg')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">{esc(a["county"]).upper()}</p>
    <h1>Car Lockouts in {esc(a["name"])}</h1>
    <p class="page-hero-lead">Locked out of your vehicle in {esc(a["name"])}? Call Lockout Pro SWFL.</p>
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
        <p>When you're locked out in <strong>{esc(a["name"])}</strong>, you need a specialist who comes to you. Lockout Pro SWFL is focused on vehicle lockouts throughout {esc(a["county"])}.</p>
        <p>Call <strong>{PHONE_DISPLAY}</strong>. Have your vehicle year, make, and model ready.</p>
      </div>
      <section class="content-block">
        <h2>Lockout Services in {esc(a["name"])}</h2>
        <ul class="text-list">{service_links}</ul>
      </section>
      <section class="content-block">
        <h2>Why Drivers in {esc(a["name"])} Call Us</h2>
        <ul class="check-list">
          <li>Focused on vehicle lockouts — not a general locksmith catch-all</li>
          <li>24/7 emergency lockout response</li>
          <li>Mobile service to your location</li>
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
      <p class="eyebrow">{esc(a["name"]).upper()} LOCKOUT</p>
      <h2>Locked Out in {esc(a["name"])}?</h2>
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
        f"Resource Center | Vehicle Lockout Guides | {BRAND}",
        "Practical vehicle lockout guides for Southwest Florida drivers.",
        f"{DOMAIN}/resources/",
        schemas=[item_list, crumb_schema],
    )}
<body class="inner-page">
<a class="skip-link" href="#main">Skip to content</a>
{header("resources")}
<section class="page-hero" id="main">
  <div class="page-hero-media" style="background-image:url('/assets/images/hero-collage.jpg')"></div>
  <div class="page-hero-veil"></div>
  <div class="container page-hero-content">
    <p class="eyebrow">RESOURCE CENTER</p>
    <h1>Lockout Guides</h1>
    <p class="page-hero-lead">Clear answers for vehicle lockouts — written for Southwest Florida drivers.</p>
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
            f'<section class="content-block"><h2>{esc(h)}</h2><p>{esc(p)}</p></section>'
            for h, p in r["sections"]
        )
        others = "".join(
            f'<li><a href="/resources/{o["slug"]}/">{esc(o["title"])}</a></li>'
            for o in RESOURCES if o["slug"] != r["slug"]
        )
        crumb_nav, crumb_schema = breadcrumbs([("Home", "/"), ("Resources", "/resources/"), (r["title"], None)])
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
        html = f'''{head(f"{r['title']} | {BRAND}", r["meta_desc"], f"{DOMAIN}/resources/{r['slug']}/", og_image=DOMAIN + r["image"], schemas=[article_schema, crumb_schema, faq_schema(r["faqs"])], article=True)}
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
    <article class="page-main article-main">
      <div class="content-block intro-block">
        <p>{esc(r["intro"])}</p>
        <p>Need lockout help now? Call <a href="tel:{PHONE_TEL}"><strong>{PHONE_DISPLAY}</strong></a>.</p>
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
      <p class="eyebrow">STILL LOCKED OUT?</p>
      <h2>Call Lockout Pro SWFL</h2>
    </div>
    <a class="btn btn-primary btn-xl" href="tel:{PHONE_TEL}">CALL {PHONE_DISPLAY}</a>
  </div>
</section>
{footer()}
</body>
</html>'''
        write(ROOT / "resources" / r["slug"] / "index.html", html)

    for old_slug, (target, msg) in RESOURCE_REDIRECTS.items():
        title = old_slug.replace("-", " ").title()
        write(
            ROOT / "resources" / old_slug / "index.html",
            redirect_page(title, msg, target, f"{DOMAIN}/resources/{old_slug}/"),
        )


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

    body = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, pri, freq in urls:
        body.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>""")
    body.append("</urlset>")
    write(ROOT / "sitemap.xml", "\n".join(body) + "\n")
    write(ROOT / "robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    service_lines = "\n".join(f"- {s['name']}: {DOMAIN}/services/{s['slug']}/" for s in SERVICES)
    city_lines = "\n".join(f"- {a['name']}: {DOMAIN}/locations/{a['slug']}/" for a in AREAS)
    article_lines = "\n".join(f"- {r['title']}: {DOMAIN}/resources/{r['slug']}/" for r in RESOURCES)
    write(
        ROOT / "llms.txt",
        f"""# {BRAND}

Website:
{DOMAIN}/

Business:
{BRAND}

Description:
Automotive lockout specialist serving Southwest Florida. Primary focus: car lockouts, emergency vehicle lockouts, trunk lockouts, fleet and commercial vehicle lockouts.

Phone:
{PHONE_DISPLAY}

Business Type:
Automotive Lockout Specialist (vehicle lockouts)

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

Related Company:
A Good Locksmith (keys, programming, residential & commercial): {AGL}

Website Purpose:
Help drivers locked out of their vehicles in Southwest Florida quickly reach Lockout Pro SWFL.
""",
    )


def main():
    build_service_pages()
    build_location_pages()
    build_resource_pages()
    build_sitemap_and_llms()
    print("Lockout-focused pages generated.")


if __name__ == "__main__":
    main()
