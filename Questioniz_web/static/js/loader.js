var q_btn= document.querySelector("#send_text-btn");
q_btn.addEventListener("click", function() {
    console.log("show_loading");
    document.querySelector("#loading").classList.remove("no-display");
});
