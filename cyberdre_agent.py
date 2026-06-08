#!/usr/bin/env python3
"""
CyberDRE Agent — B2B cybersecurity prospecting for NIS2/DORA/GDPR compliance
Targets: MSSPs, Telecoms, Energy, Finance, Pharma in the Balkans
"""

import anthropic
import json

SYSTEM_PROMPT = """You are CyberDRE, an expert B2B cybersecurity sales intelligence agent.

Your mission: prospect organizations in the Balkans region that need cybersecurity solutions
to comply with NIS2, DORA, and GDPR regulations.

TARGET GEOGRAPHY (Balkans):
Serbia, Croatia, Bosnia & Herzegovina, Montenegro, North Macedonia, Albania,
Slovenia, Romania, Bulgaria, Greece

TARGET SECTORS:
1. MSSPs (Managed Security Service Providers) — reseller/partner channel targets
2. Telecoms — operators subject to NIS2 essential services obligations
3. Energy — power grids, utilities subject to NIS2 critical infrastructure rules
4. Finance (Banks, Insurance, Asset Managers) — subject to DORA operational resilience
5. Pharma — subject to NIS2 important entities + GDPR for clinical data

REGULATORY CONTEXT:
- NIS2 Directive: Covers essential (energy, telecoms, water, transport, health, digital infra)
  and important entities (pharma, food, postal, manufacturing). Requires risk management,
  incident reporting within 24h/72h, supply chain security, business continuity.
- DORA (Digital Operational Resilience Act): Applies to all EU financial entities.
  Mandates ICT risk management, incident classification & reporting, resilience testing,
  third-party ICT risk management. Compliance deadline: Jan 17, 2025.
- GDPR: Applies to all entities processing EU personal data. Requires DPO, breach
  notification within 72h, data protection by design, cross-border transfer safeguards.

YOUR OUTPUT FORMAT for each prospect:
```
COMPANY: [Name]
COUNTRY: [Balkans country]
SECTOR: [MSSP/Telecom/Energy/Finance/Pharma]
REGULATIONS: [NIS2 / DORA / GDPR — applicable ones]
SIZE: [estimated employees or revenue]
WEBSITE: [URL if found]
COMPLIANCE GAPS: [specific security gaps based on sector/regulation]
CYBERSECURITY NEEDS: [SOC, SIEM, EDR, GRC platform, pen testing, incident response, etc.]
CONTACT HINTS: [CISO, CTO, CIO, Compliance Officer, DPO — likely decision makers]
OPPORTUNITY SCORE: [High/Medium/Low + brief rationale]
---
```

Search systematically by country and sector. Prioritize publicly listed companies,
regulated entities, and organizations that have disclosed cyber incidents or audits.
Focus on companies with 200+ employees or €50M+ revenue where regulation exposure is highest.
"""

BALKANS_COUNTRIES = [
    "Serbia", "Croatia", "Bosnia Herzegovina", "Montenegro",
    "North Macedonia", "Albania", "Slovenia", "Romania", "Bulgaria", "Greece"
]

SECTORS = ["MSSP", "Telecom", "Energy", "Finance", "Pharma"]

SEARCH_QUERIES = [
    # NIS2 essential entities
    "NIS2 compliance telecom operator {country} cybersecurity",
    "energy utility company {country} OT security NIS2",
    # DORA financial entities
    "bank financial institution {country} DORA compliance ICT risk",
    "insurance company {country} digital operational resilience DORA",
    # Pharma + GDPR
    "pharmaceutical company {country} GDPR clinical data cybersecurity",
    # MSSPs as channel partners
    "MSSP managed security service provider {country} SOC services",
    # General sector search
    "{sector} company {country} cybersecurity regulation compliance",
]


def build_prospecting_prompt(country: str, sector: str) -> str:
    return f"""Search for {sector} companies in {country} that are subject to NIS2, DORA, or GDPR regulations.

Find at least 3-5 specific organizations. For each company:
1. Search for their name, size, and website
2. Identify which regulations apply to them based on their sector and EU/EEA status
3. Look for any public information about their cybersecurity posture, incidents, or compliance efforts
4. Identify likely cybersecurity gaps and needs
5. Find decision-maker titles (CISO, CTO, DPO, Compliance Officer)

Search queries to use:
- "{sector} company {country} cybersecurity"
- "{sector} {country} NIS2 OR DORA OR GDPR compliance"
- "largest {sector} organizations {country}"

Output each prospect in the specified format."""


def run_prospecting_agent(countries: list[str] = None, sectors: list[str] = None):
    client = anthropic.Anthropic()

    target_countries = countries or BALKANS_COUNTRIES[:3]  # default: first 3 for demo
    target_sectors = sectors or SECTORS

    all_leads = []

    print("=" * 70)
    print("CyberDRE Agent — NIS2/DORA/GDPR Prospecting in the Balkans")
    print("=" * 70)
    print(f"Countries: {', '.join(target_countries)}")
    print(f"Sectors:   {', '.join(target_sectors)}")
    print("=" * 70)

    for country in target_countries:
        for sector in target_sectors:
            print(f"\n[PROSPECTING] {sector} in {country}...")
            print("-" * 50)

            user_prompt = build_prospecting_prompt(country, sector)

            try:
                with client.messages.stream(
                    model="claude-opus-4-8",
                    max_tokens=4096,
                    thinking={"type": "adaptive"},
                    system=SYSTEM_PROMPT,
                    tools=[
                        {
                            "type": "web_search_20260209",
                            "name": "web_search",
                        }
                    ],
                    messages=[
                        {"role": "user", "content": user_prompt}
                    ],
                ) as stream:
                    response = stream.get_final_message()

                # Extract text content from response
                result_text = ""
                for block in response.content:
                    if block.type == "text":
                        result_text += block.text

                if result_text:
                    print(result_text)
                    all_leads.append({
                        "country": country,
                        "sector": sector,
                        "leads": result_text,
                    })
                else:
                    print(f"  No text output for {sector}/{country}")

            except anthropic.APIError as e:
                print(f"  API error for {sector}/{country}: {e}")

    # Save results to JSON
    output_file = "cyberdre_leads.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_leads, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 70)
    print(f"Prospecting complete. Results saved to {output_file}")
    print(f"Total segments prospected: {len(all_leads)}")
    print("=" * 70)

    return all_leads


def run_single_query(query: str):
    """Run a single ad-hoc prospecting query."""
    client = anthropic.Anthropic()

    print(f"\n[QUERY] {query}\n")

    with client.messages.stream(
        model="claude-opus-4-8",
        max_tokens=4096,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        tools=[
            {
                "type": "web_search_20260209",
                "name": "web_search",
            }
        ],
        messages=[
            {"role": "user", "content": query}
        ],
    ) as stream:
        response = stream.get_final_message()

    for block in response.content:
        if block.type == "text":
            print(block.text)

    return response


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        # Ad-hoc query mode: python cyberdre_agent.py "find banks in Serbia for DORA"
        query = " ".join(sys.argv[1:])
        run_single_query(query)
    else:
        # Full prospecting run — customize countries/sectors as needed
        run_prospecting_agent(
            countries=["Serbia", "Croatia", "Romania"],
            sectors=["Finance", "Telecom", "Energy", "Pharma", "MSSP"],
        )
