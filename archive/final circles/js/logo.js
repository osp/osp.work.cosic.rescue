/*
$(document).ready( function(){

	var canvas = document.getElementById('logoCanvas1');
	var ctx = canvas.getContext('2d');

	var	pattern1 = new Image();
	pattern1.onload = function(){
		ctx.save();
		ctx.translate(pattern1.width/2, pattern1.height/2);
		ctx.rotate(45 * Math.PI/180);
		ctx.drawImage(pattern1, (-pattern1.width/2), (-pattern1.height/2));
		ctx.restore();
	};
	pattern1.src = '1.1.svg';

//	ctx.save();

//	ctx.rotate(Math.PI*2/180);

	var canvas2 = document.getElementById('logoCanvas2');
	var ctx2 = canvas.getContext('2d');

	var pattern2 = new Image();
	pattern2.onload = function(){
		ctx2.save();
		ctx2.translate(pattern1.width/2, pattern1.height/2);
		ctx2.rotate(Math.PI*65/180);
		ctx2.translate((-pattern2.width/2),(-pattern2.height/2));
		ctx2.drawImage(pattern2, 20, 20);
		ctx2.restore();
	};
	pattern2.src = '2.1.svg';

});
*/


$(document).ready( function(){

	var patterns = new Array( '1.1.svg', '2.1.svg', '2.2.svg', '2.3.svg', '3.1.svg', '3.2.svg', '3.3.svg', '4.1.svg', '4.2.svg', '4.3.svg', '5.1.svg', '5.2.svg', '5.3.svg', '6.1.svg', '6.3.svg', '7.1.svg', '7.2.svg' );

	var pick = Math.floor(Math.random() * patterns.length);
/*
	$('#logo').append('<img id="pattern1" src="' + patterns[Math.floor(Math.random() * patterns.length)] + '" />').find('#pattern1').css('position', 'absolute').hide();
	$('#logo').append('<img id="pattern2" src="' + patterns[Math.floor(Math.random() * patterns.length)] + '" />').find('#pattern2').css('position','absolute').hide();
*/

	var object1 = '<!--[if !IE]>-->' + "\n" + '<object data="' + patterns[Math.floor(Math.random() * patterns.length)] + '" type="image/svg+xml" width="90" height="90" id="pattern1">' + "\n" + '<!--<![endif]-->' + "\n" + '<!--[if lt IE 9]>' + "\n" + '<object src="' + patterns[Math.floor(Math.random() * patterns.length)] + '" classid="image/svg+xml" width="90" height="90" id="pattern1">' + "\n" + '<![endif]-->' + "\n" + '<!--[if gte IE 9]>' + "\n" + '<object data="' + patterns[Math.floor(Math.random() * patterns.length)] + '" type="image/svg+xml" width="90" height="90" id="pattern1">' + "\n" + '<![endif]-->' + "\n" + '<h1>Put optional fallback content here</h1> </object>'

	var object2 = '<!--[if !IE]>-->' + "\n" + '<object data="' + patterns[Math.floor(Math.random() * patterns.length)] + '" type="image/svg+xml" width="90" height="90" id="pattern2">' + "\n" + '<!--<![endif]-->' + "\n" + '<!--[if lt IE 9]>' + "\n" + '<object src="' + patterns[Math.floor(Math.random() * patterns.length)] + '" classid="image/svg+xml" width="90" height="90" id="pattern2">' + "\n" + '<![endif]-->' + "\n" + '<!--[if gte IE 9]>' + "\n" + '<object data="' + patterns[Math.floor(Math.random() * patterns.length)] + '" type="image/svg+xml" width="90" height="90" id="pattern2">' + "\n" + '<![endif]-->' + "\n" + '<h1>Put optional fallback content here</h1> </object>'

	$('#logo').append(object1).find('#pattern1').css('position', 'absolute').hide();
	$('#logo').append(object2).find('#pattern2').css('position', 'absolute').hide();

	var p1 = $('#pattern1');
	var p2 = $('#pattern2');

	var r1 = Math.floor(Math.random() * 360);
	var r2 = Math.floor(Math.random() * 360);

	p1.rotate(r1);
	p1.css({ 'left' : '32px', 'top' : '32px' }).show();
	p2.rotate(r2);
	p2.css({ 'left' : '56px', 'top' : '56px' }).show();

});

