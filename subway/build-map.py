#!/usr/bin/env python3
"""Build the Zoom API tube-style map.

40 of Zoom's APIs grouped onto 8 product lines.
"""

import sys
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

ABBREV = {
    "Revenue Accelerator":  "Revenue Accel.",
    "Workforce Management": "Workforce Mgmt",
    "Quality Management":   "Quality Mgmt",
    "Number Management":    "Number Mgmt",
    "Video Management":     "Video Mgmt",
    "Virtual Agent":        "Virtual Agent",
    "Contact Center":       "Contact Center",
    "Auto Dialer":          "Auto Dialer",
    "AI Companion":         "AI Companion",
    "Team Chat":            "Team Chat",
    "Instant Message":      "Instant Msg",
}

LINES = [
    {
        "name": "Meetings & Events",
        "color": "#2D8CFF",  # Zoom blue
        "stations": [
            ("Meeting", (260, 200)),
            ("Webinar", (430, 175)),
            ("Events",  (600, 165)),
            ("Phone",   (770, 175)),
            ("Rooms",   (940, 200)),
        ],
    },
    {
        "name": "Communication",
        "color": "#E0245E",
        "stations": [
            ("Chat",            (260, 305)),
            ("Team Chat",       (400, 285)),
            ("Instant Message", (560, 285)),
            ("Mail",            (700, 305)),
            ("Calendar",        (840, 285)),
            ("Scheduler",       (980, 305)),
        ],
    },
    {
        "name": "Account & Identity",
        "color": "#0E9D6E",
        "stations": [
            ("Account",       (260, 410)),
            ("User",          (390, 430)),
            ("Group",         (520, 430)),
            ("Device",        (650, 430)),
            ("Number Management",(800, 410)),
            ("SCIM2",         (950, 430)),
        ],
    },
    {
        "name": "Recordings & Reports",
        "color": "#7B3FE4",
        "stations": [
            ("Recording", (290, 540)),
            ("Report",    (440, 520)),
            ("Metrics",   (590, 540)),
            ("Quality Management",(770, 520)),
        ],
    },
    {
        "name": "AI & Automation",
        "color": "#C5318B",
        # Closed quadrilateral.
        "closed": True,
        "stations": [
            ("AI Companion",  (820, 590)),
            ("Virtual Agent", (905, 660)),
            ("Auto Dialer",   (820, 730)),
            ("Chatbot",       (735, 660)),
        ],
    },
    {
        "name": "Apps & Marketplace",
        "color": "#E68B1F",
        "stations": [
            ("Marketplace", (270, 640)),
            ("Docs",        (400, 620)),
            ("Tasks",       (520, 620)),
            ("Whiteboard",  (640, 620)),
            ("Clips",       (700, 700)),
        ],
    },
    {
        "name": "Contact Center & Workforce",
        "color": "#1E5BD0",
        "stations": [
            ("Contact Center",      (260, 745)),
            ("Revenue Accelerator", (435, 720)),
            ("Workforce Management",(615, 745)),
            ("Commerce",            (790, 720)),
        ],
    },
    {
        "name": "SDKs & Industry",
        "color": "#5A6275",
        "stations": [
            ("Healthcare",       (270, 815)),
            ("Video Management", (430, 815)),
            ("Video SDK",        (570, 815)),
            ("Meeting SDK",      (700, 815)),
            ("Cobrowse SDK",     (840, 815)),
            ("CRC",              (970, 815)),
        ],
    },
]

URL_OVERRIDES = {
    "Meeting":              "https://apis.apis.io/apis/zoom/zoom-meeting-api/",
    "Webinar":              "https://apis.apis.io/apis/zoom/zoom-webinar-api/",
    "Events":               "https://apis.apis.io/apis/zoom/zoom-events-api/",
    "Phone":                "https://apis.apis.io/apis/zoom/zoom-phone-api/",
    "Rooms":                "https://apis.apis.io/apis/zoom/zoom-rooms-api/",
    "Chat":                 "https://apis.apis.io/apis/zoom/zoom-chat-api/",
    "Team Chat":            "https://apis.apis.io/apis/zoom/zoom-team-chat-api/",
    "Instant Message":      "https://apis.apis.io/apis/zoom/zoom-instant-message-api/",
    "Mail":                 "https://apis.apis.io/apis/zoom/zoom-mail-api/",
    "Calendar":             "https://apis.apis.io/apis/zoom/zoom-calendar-api/",
    "Scheduler":            "https://apis.apis.io/apis/zoom/zoom-scheduler-api/",
    "Account":              "https://apis.apis.io/apis/zoom/zoom-account-api/",
    "User":                 "https://apis.apis.io/apis/zoom/zoom-user-api/",
    "Group":                "https://apis.apis.io/apis/zoom/zoom-group-api/",
    "Device":               "https://apis.apis.io/apis/zoom/zoom-device-api/",
    "Number Management":    "https://apis.apis.io/apis/zoom/zoom-number-management-api/",
    "SCIM2":                "https://apis.apis.io/apis/zoom/zoom-scim2-api/",
    "Recording":            "https://apis.apis.io/apis/zoom/zoom-recording-api/",
    "Report":               "https://apis.apis.io/apis/zoom/zoom-report-api/",
    "Metrics":              "https://apis.apis.io/apis/zoom/zoom-metrics-api/",
    "Quality Management":   "https://apis.apis.io/apis/zoom/zoom-quality-management-api/",
    "AI Companion":         "https://apis.apis.io/apis/zoom/zoom-ai-companion-api/",
    "Virtual Agent":        "https://apis.apis.io/apis/zoom/zoom-virtual-agent-api/",
    "Auto Dialer":          "https://apis.apis.io/apis/zoom/zoom-auto-dialer-api/",
    "Chatbot":              "https://apis.apis.io/apis/zoom/zoom-chatbot-api/",
    "Marketplace":          "https://apis.apis.io/apis/zoom/zoom-marketplace-api/",
    "Docs":                 "https://apis.apis.io/apis/zoom/zoom-docs-api/",
    "Tasks":                "https://apis.apis.io/apis/zoom/zoom-tasks-api/",
    "Whiteboard":           "https://apis.apis.io/apis/zoom/zoom-whiteboard-api/",
    "Clips":                "https://apis.apis.io/apis/zoom/zoom-clips-api/",
    "Contact Center":       "https://apis.apis.io/apis/zoom/zoom-contact-center-api/",
    "Revenue Accelerator":  "https://apis.apis.io/apis/zoom/zoom-revenue-accelerator-api/",
    "Workforce Management": "https://apis.apis.io/apis/zoom/zoom-workforce-management-api/",
    "Commerce":             "https://apis.apis.io/apis/zoom/zoom-commerce-api/",
    "Healthcare":           "https://apis.apis.io/apis/zoom/zoom-healthcare-api/",
    "Video Management":     "https://apis.apis.io/apis/zoom/zoom-video-management-api/",
    "Video SDK":            "https://apis.apis.io/apis/zoom/zoom-video-sdk-api/",
    "Meeting SDK":          "https://apis.apis.io/apis/zoom/zoom-meeting-sdk/",
    "Cobrowse SDK":         "https://apis.apis.io/apis/zoom/zoom-cobrowse-sdk-api/",
    "CRC":                  "https://apis.apis.io/apis/zoom/zoom-crc-api/",
}


def main():
    seen = set()
    n_unique = 0
    for ln in LINES:
        for (st, _) in ln["stations"]:
            if st not in seen:
                n_unique += 1
                seen.add(st)
    build_subway(
        title="The Zoom API · Underground Map",
        subtitle=f"{n_unique} APIs · {len(LINES)} functional lines · click any station for the apis.io page",
        lines=LINES,
        abbrev=ABBREV,
        source_label="Source: zoom/openapi/*.yml · github.com/api-evangelist/zoom",
        out_dir=Path(__file__).resolve().parent,
        out_basename="zoom-subway-map",
        provider_id="zoom",
        station_url_overrides=URL_OVERRIDES,
    )


if __name__ == "__main__":
    main()
