function renderCusdis() {
  const el = document.getElementById("cusdis_thread");
  if (el && window.CUSDIS) {
    window.CUSDIS.renderTo(el);
    // Give the iframe time to load before applying theme
    setTimeout(applyCusdisTheme, 800);
  }
}

function applyCusdisTheme() {
  const iframe = document.querySelector("#cusdis_thread iframe");
  if (!iframe) return;

  const scheme = document.documentElement.getAttribute("data-md-color-scheme");
  const theme = scheme === "slate" ? "dark" : "light";

  iframe.contentWindow.postMessage(
    {
      from: "cusdis",
      event: "setTheme",
      theme: theme,
    },
    "*"
  );
}

// Run once on page load
document.addEventListener("DOMContentLoaded", renderCusdis);

// Re-run when Material swaps page content (instant loading)
document.addEventListener("DOMContentSwitch", renderCusdis);

// Re-apply when theme toggles
const observer = new MutationObserver(() => {
  // Give iframe time to exist if just rendered
  setTimeout(applyCusdisTheme, 300);
});
observer.observe(document.documentElement, {
  attributes: true,
  attributeFilter: ["data-md-color-scheme"],
});