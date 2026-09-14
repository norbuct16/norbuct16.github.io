// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
navToggle.addEventListener('click', () => {
  const open = navLinks.classList.toggle('is-open');
  navToggle.classList.toggle('is-open', open);
  navToggle.setAttribute('aria-expanded', open);
});
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('is-open');
    navToggle.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', false);
  });
});

// Header shadow on scroll
const header = document.getElementById('siteHeader');
window.addEventListener('scroll', () => {
  header.classList.toggle('is-scrolled', window.scrollY > 8);
}, { passive: true });

// Scroll-spy for active nav link
const sections = ['about', 'work', 'experience', 'skills', 'contact']
  .map(id => document.getElementById(id))
  .filter(Boolean);
const navAnchors = Array.from(navLinks.querySelectorAll('a.nav-link'));
const spy = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.getAttribute('id');
      navAnchors.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + id));
    }
  });
}, { rootMargin: '-40% 0px -50% 0px' });
sections.forEach(s => spy.observe(s));

// Note: the résumé download links and the footer copyright year are now
// rendered server-side (see app.py / templates), so no JS is needed for them.
