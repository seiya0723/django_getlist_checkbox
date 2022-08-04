window.addEventListener("load" , function (){

	target_body		= document.getElementById("test");
	target_body.innerHTML	= "Hello World !!"

});


function greet(name){ //←この関数内だけで有効な変数であるnameが宣言される。(値は関数呼び出し時に指定する引数)
    console.log("こんにちは" + name);
}


greet("Bob");
