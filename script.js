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

  // Reviews carousel — mounts when written reviews exist (name + text required)
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

    const escapeHtml = (value) =>
      String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");

    track.innerHTML = reviews
      .map((r) => {
        const source =
          r.source === "Google"
            ? `<span class="review-source" aria-label="Google review">Google</span>`
            : "";
        const profile = r.profile
          ? `<span class="review-profile">${escapeHtml(r.profile)}</span>`
          : "";
        const age = r.age
          ? `<span class="review-age">${escapeHtml(r.age)}</span>`
          : "";

        return `
      <article class="review-card" data-review-type="${escapeHtml(r.type || "real")}">
        <div class="review-card-top">
          <span class="review-stars" aria-hidden="true">★★★★★</span>
          ${source}
        </div>
        <p class="review-text is-clamped">“${escapeHtml(r.text)}”</p>
        <button type="button" class="review-toggle" hidden>Read more</button>
        <div class="review-meta">
          <strong class="review-name">${escapeHtml(r.name)}</strong>
          ${profile}
          ${age}
        </div>
      </article>`;
      })
      .join("");

    // Enable Read more only when text actually overflows the clamp
    const setupExpandable = () => {
      track.querySelectorAll(".review-card").forEach((card) => {
        const text = card.querySelector(".review-text");
        const toggle = card.querySelector(".review-toggle");
        if (!text || !toggle) return;
        text.classList.add("is-clamped");
        const overflows = text.scrollHeight > text.clientHeight + 2;
        toggle.hidden = !overflows;
        toggle.textContent = "Read more";
        toggle.setAttribute("aria-expanded", "false");
        toggle.onclick = () => {
          const expanded = text.classList.contains("is-clamped");
          text.classList.toggle("is-clamped", !expanded);
          toggle.textContent = expanded ? "Read less" : "Read more";
          toggle.setAttribute("aria-expanded", String(expanded));
          if (expanded) stopAuto();
          else startAuto();
        };
      });
    };
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
      const list = cards();
      const card = list[index];
      if (card && list[0]) {
        track.scrollTo({
          left: card.offsetLeft - list[0].offsetLeft,
          behavior: "smooth",
        });
      }
      renderDots();
    };

    prevBtn?.addEventListener("click", () => go(index - 1));
    nextBtn?.addEventListener("click", () => go(index + 1));
    dotsWrap?.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-i]");
      if (btn) go(Number(btn.dataset.i));
    });

    // Touch / swipe support
    let touchStartX = 0;
    track.addEventListener(
      "touchstart",
      (e) => {
        touchStartX = e.changedTouches[0].screenX;
      },
      { passive: true }
    );
    track.addEventListener(
      "touchend",
      (e) => {
        const delta = e.changedTouches[0].screenX - touchStartX;
        if (Math.abs(delta) < 40) return;
        if (delta < 0) go(index + 1);
        else go(index - 1);
      },
      { passive: true }
    );

    let autoTimer = null;
    const startAuto = () => {
      stopAuto();
      if (cards().length <= pageSize()) return;
      autoTimer = window.setInterval(() => {
        go(index >= maxIndex() ? 0 : index + 1);
      }, 7000);
    };
    const stopAuto = () => {
      if (autoTimer) window.clearInterval(autoTimer);
      autoTimer = null;
    };

    root.addEventListener("mouseenter", stopAuto);
    root.addEventListener("mouseleave", startAuto);
    root.addEventListener("focusin", stopAuto);
    root.addEventListener("focusout", startAuto);
    window.addEventListener("resize", () => go(Math.min(index, maxIndex())));

    setupExpandable();
    window.addEventListener("resize", setupExpandable);
    renderDots();
    go(0);
    startAuto();
  }
})();
