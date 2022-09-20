const printBtn = document.getElementById("print")


document.querySelectorAll('.slider').forEach(slider => {
    slider.addEventListener('input', function(e) {
         if (this.id == 'thk_factor') {
            document.getElementsByName("tf")[0].textContent = this.value;
        }
        else if (this.id == 'water') {
            document.getElementsByName("hydration")[0].textContent = this.value + "%";
        }
    })
})


function tfWeight() {
    const doughWt = document.getElementById('id_dough_wt_set');
    const pizzaSz = document.getElementById('id_pizza_size_set');

    if (document.getElementById('id_choice_set_0').checked) {
        document.getElementById('choice-wt').style.display = "block";
        document.getElementById('choice-tf').style.display = "none";
        pizzaSz.required = false;
        doughWt.required = true;
        pizzaSz.value = 16;

    }
    else {
        document.getElementById('choice-wt').style.display = "none";
        document.getElementById('choice-tf').style.display = "block";
        pizzaSz.required = true;
        doughWt.required = false;
        doughWt.value = "";
    }
}

tfWeight();


function hideShowPrint() {
    if (document.getElementById('recipe')) {
        printBtn.hidden = false;
    }
    else {
        printBtn.hidden = true;
    }
}

hideShowPrint();


printBtn.addEventListener("click", () => { window.print(); });

document.getElementById('choice').addEventListener("change", tfWeight);
