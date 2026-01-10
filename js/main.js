// The NICEHR Group - Main JavaScript
// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function() {
      navLinks.classList.toggle('active');
      navToggle.classList.toggle('active');
    });
  }

  // Close mobile menu when clicking a link (but not dropdown toggles)
  const links = navLinks?.querySelectorAll('a:not(.nav-dropdown > .nav-link)');
  links?.forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
      navToggle?.classList.remove('active');
    });
  });

  // Mobile dropdown toggle - tap to open/close submenus
  const dropdowns = document.querySelectorAll('.nav-dropdown');
  dropdowns.forEach(dropdown => {
    const toggle = dropdown.querySelector('.nav-link');
    if (toggle) {
      toggle.addEventListener('click', function(e) {
        // Only handle on mobile (when nav toggle is visible)
        if (window.innerWidth <= 968) {
          e.preventDefault();
          // Close other dropdowns
          dropdowns.forEach(d => {
            if (d !== dropdown) d.classList.remove('active');
          });
          // Toggle this dropdown
          dropdown.classList.toggle('active');
        }
      });
    }
  });

  // Close dropdowns when clicking outside
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.nav-dropdown')) {
      dropdowns.forEach(d => d.classList.remove('active'));
    }
  });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Add scroll animation to elements
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);

  // Observe cards and sections for animation
  document.querySelectorAll('.card, .stat-item, .team-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });

  // Nav background on scroll
  const nav = document.querySelector('.nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        nav.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
      } else {
        nav.style.boxShadow = 'none';
      }
    });
  }

  // Form submission handler (placeholder)
  const contactForm = document.querySelector('.contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      alert('Thank you for your message! We will get back to you within 24 hours.');
      this.reset();
    });
  }

  // Dynamic copyright year range
  const startYear = 2012;
  const year = new Date().getFullYear();
  const copyrightEl = document.getElementById("copyrightYear");
  if (copyrightEl) copyrightEl.textContent = year > startYear ? `${startYear}–${year}` : `${year}`;
});

// Console message
console.log('%c🏥 The NICEHR Group', 'font-size: 24px; font-weight: bold; color: #1a365d;');
console.log('%cHealthcare IT. Simplified.', 'font-size: 14px; color: #6b7280;');
