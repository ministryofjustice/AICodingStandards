---
inclusion: fileMatch
fileMatchPattern: '**/*.{html,css,scss,tsx,jsx,vue,js,ts}'
description: MoJ frontend and accessibility standards
---

# MoJ Frontend Standards

## HTML and CSS standards

Use semantic HTML and accessibility attributes (ARIA). Minimise !important; maintain specificity hierarchy.
Avoid inline styles; use external stylesheets or CSS-in-JS. Keep CSS modular (e.g. BEM, CSS Modules, Tailwind).


## JavaScript/TypeScript frontend

Enforce strict typing with TypeScript. Use ES6+. Implement error handling; avoid silent failures.
Avoid global variables; use modules or closures. Use ESLint. Prefer React, Angular, or Vue as approved; state management Redux or Zustand.


## Accessibility (WCAG AA)

Meet WCAG 2.2 Level AA as the internal standard (WCAG 2.1 Level AA is the external supplier minimum).
Use GOV.UK Design System components. Alt text for images, ARIA for dynamic elements, keyboard navigation, focus management.
Test with screen readers and automated tools (Axe, Pa11y, WAVE) AND with real users using assistive technologies.
Support browser zoom to 400%; logical headings; meaningful link text; descriptive page titles; colour contrast.
Design accessibility in from the start: include accessibility requirements in user stories and acceptance criteria,
test each sprint, include accessibility checks in code review, and remediate defects with same priority as security bugs.


## Government Service Manual

Follow the Government Service Design Manual. Services are assessed against it before going live.
Use verified browsers list; responsive design; progressive enhancement.

