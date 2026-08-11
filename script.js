(() => {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".menu-toggle");
  const mobileNav = document.querySelector("#mobile-nav");

  const onScroll = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 24);
  };

  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  if (toggle && mobileNav) {
    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      if (open) {
        mobileNav.setAttribute("hidden", "");
      } else {
        mobileNav.removeAttribute("hidden");
      }
    });

    mobileNav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        toggle.setAttribute("aria-expanded", "false");
        mobileNav.setAttribute("hidden", "");
      });
    });
  }

  const revealItems = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && revealItems.length) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    revealItems.forEach((el) => io.observe(el));
  } else {
    revealItems.forEach((el) => el.classList.add("is-in"));
  }

  // Reviews carousel — only mounts when real reviews exist
  const reviews = Array.isArray(window.LOCKOUT_PRO_REVIEWS)
    ? window.LOCKOUT_PRO_REVIEWS.filter((r) => r && r.text && r.name)
    : [];
  const root = document.querySelector("[data-reviews-root]");
  const track = document.querySelector("[data-reviews-track]");
  const dotsWrap = document.querySelector("[data-reviews-dots]");
  const prevBtn = document.querySelector(".reviews-prev");
  const nextBtn = document.querySelector(".reviews-next");

  if (root && track && reviews.length) {
    root.hidden = false;

    const stars = (n) => {
      const rating = Math.max(0, Math.min(5, Number(n) || 0));
      return "★★★★★".slice(0, Math.round(rating)) + "☆☆☆☆☆".slice(Math.round(rating));
    };

    track.innerHTML = reviews
      .map(
        (r) => `
      <article class="review-card">
        <div class="review-card-top">
          <span class="review-stars" aria-label="${Number(r.rating) || 5} out of 5 stars">${stars(r.rating || 5)}</span>
          ${r.source ? `<span class="review-source">${r.source}</span>` : ""}
        </div>
        <p class="review-text">“${String(r.text).replace(/</g, "&lt;")}”</p>
        <div class="review-meta">
          <strong>${String(r.name).replace(/</g, "&lt;")}</strong>
          ${r.meta ? `<span>${String(r.meta).replace(/</g, "&lt;")}</span>` : ""}
        </div>
      </article>`
      )
      .join("");

    let index = 0;
    const cards = () => Array.from(track.children);
    const pageSize = () => (window.innerWidth < 700 ? 1 : window.innerWidth < 1000 ? 2 : 3);

    const maxIndex = () => Math.max(0, cards().length - pageSize());

    const renderDots = () => {
      if (!dotsWrap) return;
      const pages = maxIndex() + 1;
      dotsWrap.innerHTML = Array.from({ length: pages }, (_, i) =>
        `<button type="button" class="reviews-dot${i === index ? " is-active" : ""}" aria-label="Go to review set ${i + 1}" data-i="${i}"></button>`
      ).join("");
    };

    const go = (i) => {
      index = Math.max(0, Math.min(maxIndex(), i));
      const card = cards()[index];
      if (card) {
        track.scrollTo({ left: card.offsetLeft - track.offsetLeft, behavior: "smooth" });
      }
      renderDots();
    };

    prevBtn?.addEventListener("click", () => go(index - 1));
    nextBtn?.addEventListener("click", () => go(index + 1));
    dotsWrap?.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-i]");
      if (btn) go(Number(btn.dataset.i));
    });

    let autoTimer = null;
    const startAuto = () => {
      stopAuto();
      if (cards().length <= pageSize()) return;
      autoTimer = window.setInterval(() => {
        go(index >= maxIndex() ? 0 : index + 1);
      }, 5200);
    };
    const stopAuto = () => {
      if (autoTimer) window.clearInterval(autoTimer);
      autoTimer = null;
    };

    root.addEventListener("mouseenter", stopAuto);
    root.addEventListener("mouseleave", startAuto);
    window.addEventListener("resize", () => go(Math.min(index, maxIndex())));

    renderDots();
    go(0);
    startAuto();
  }
})();
