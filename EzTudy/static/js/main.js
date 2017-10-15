const btn_main = document.getElementById('btn_main');
const btn_mid = document.getElementById('btn_mid');
const div_res = document.getElementById('div_res')
div_res.style.display ='none'

btn_main.addEventListener("click", btMain)
btn_mid.addEventListener("click", btMid)

function btMain(){
	if(btn_main.className == 'btn-main'){
		btn_main.classList.add('active')
	} else {
		btn_main.classList.remove('active')
	}
}
function btMid(){
	if (div_res.style.display =='block'){
		div_res.style.display = 'none'
        return
    }
	div_res.style.display ='block'
}
