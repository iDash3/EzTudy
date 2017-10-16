const btn_mid = document.getElementById('btn_mid');
const div_res = document.getElementById('div_res')
div_res.style.display ='none'

btn_mid.addEventListener("click", btMid)


function btMid(){
	if (div_res.style.display =='block'){
		div_res.style.display = 'none'
        return
    }
	div_res.style.display ='block'
}
