document.addEventListener("DOMContentLoaded", function () {
  const iframe = document.querySelector("#cusdis_thread iframe");
  const html = document.documentElement;

  if (!iframe) return;

  const applyTheme = () => {
    const scheme = html.getAttribute("data-md-color-scheme");
    const theme = scheme === "default" ? "light" : "dark";
    iframe.contentWindow.postMessage(
      {
        from: "cusdis",
        event: "setTheme",
        theme: theme,
      },
      "*"
    );
  };

  // Initial
  applyTheme();

  // React on changes (when user toggles theme in Material)
  const observer = new MutationObserver(applyTheme);
  observer.observe(html, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
});