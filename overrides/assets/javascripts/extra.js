// Auto light/dark mode
function initCusdis() {
  const el = document.getElementById("cusdis_thread");
  if (el && window.CUSDIS) {
    window.CUSDIS.renderTo(el);
  }
}

function setCusdisTheme() {
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

document.addEventListener("DOMContentLoaded", () => {
  initCusdis();
  // Apply theme once loaded
  setTimeout(setCusdisTheme, 500);
});

document.addEventListener("DOMContentSwitch", () => {
  initCusdis();
  setTimeout(setCusdisTheme, 500);
});

// Watch for changes to Material's scheme toggle
const observer = new MutationObserver(setCusdisTheme);
observer.observe(document.documentElement, {
  attributes: true,
  attributeFilter: ["data-md-color-scheme"],
});
// Fix comments to appear on initial load of the page
// function initCusdis() {
//   const el = document.getElementById("cusdis_thread");
//   if (el && window.CUSDIS) {
//     window.CUSDIS.renderTo(el);
//   }
// }

// document.addEventListener("DOMContentLoaded", initCusdis);
// document.addEventListener("DOMContentSwitch", initCusdis);