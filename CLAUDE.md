# The NICEHR Group Website

## Writing Doctrine
This project follows the **Enterprise Apple for Healthcare Consulting** doctrine.
See `ENTERPRISE_APPLE_DOCTRINE.md` and `AI_INSTRUCTIONS.md` for full guidelines.

**Key rules:**
- No slogans or taglines
- No promotional language (strategic, innovative, comprehensive, seamless, etc.)
- Short, declarative sentences
- Verbs over adjectives
- Outcome-focused copy

**Approved CTAs:** Explore Solutions, Talk to an Expert, Contact, Request Proposal, View Platform, View RCM

**Prohibited:** "Learn more", "Get started", "Discover", "We offer", persuasive questions

## Structure
- 22 HTML pages (static site)
- `css/` - Stylesheets
- `js/` - JavaScript
- `images/` - Assets including client logos

## Key Pages
- `index.html` - Homepage
- `services.html` - All solutions
- `rcm.html` - Revenue cycle management
- `ehr-systems.html` - EHR platform expertise
- `dischedule.html` - Behavioral matching platform

## Client Logos Section
Header must be: **"Healthcare organizations served."**
Intro line: **"Delivery experience across healthcare systems."**

## Recent Work
- Applied Enterprise Apple doctrine compliance fixes (Dec 2025)
- Renamed "IT Strategic Planning" to "IT Planning" across all navigation
- Removed taglines and promotional language
- Fixed "What We Deliver" section - wrapped cards in 3-column grid layout
- Fixed mobile responsive issues (Jan 2026):
  - Added tap/click support for mobile dropdown navigation
  - Reduced section/card/header padding on mobile
  - Fixed testimonial grid overflow
  - Added mobile nav scroll support

## Local Development
```bash
python3 -m http.server 8000
open http://localhost:8000
```
Or open `index.html` directly in browser.

## Responsive Breakpoints
- `968px` - Tablet (nav collapses, grids → 2 columns)
- `768px` - Small tablet
- `640px` - Mobile (grids → 1-2 columns)
- `480px` - Small mobile
- `380px` - Very small (single column)

Test with browser dev tools: `Cmd + Option + I` → `Cmd + Shift + M`

## Session History
- @.claude/sessions/2025-12-28-doctrine-fixes.txt - Doctrine compliance audit & fixes
- @.claude/sessions/2026-01-10-mobile-fixes.txt - Mobile responsive fixes
