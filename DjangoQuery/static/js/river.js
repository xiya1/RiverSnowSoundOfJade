// window.onload = function(){
// 			var oSkin = document.getElementById('skin');
// 			var oBtn1 = document.getElementById('btn01');
// 			var oBtn2 = document.getElementById('btn02');

// 			oBtn1.onclick = function(){
// 				oSkin.href = "css/style1.css";
// 			}
// 			oBtn2.onclick = function(){
// 				oSkin.href = "css/style2.css";
// 			}
// 		}
// alert(iNum);
// var iNum = 12;

// fnMyalert();
// function fnMyalert(){
// 	alert('hello');
// }
// window.onload = function(){
	// function fnMyalert(iNum1,iNum2){
	// 	var iNum3 = iNum1 + iNum2;
		
	// 	return iNum3;
	// 	alert('内部的iNum3 = '+iNum3);
	// }
	// var iResult = fnMyalert(2,5);
	// alert(iResult);

	// function fnChangestyle(sTr1,sTr2){
	// 	var oDiv = document.getElementById('div1');
	// 	oDiv.style[sTr1] = sTr2;
	// }

	// fnChangestyle('color','pink');
	// var oBtn = document.getElementById('btn01');
	// var oDiv = document.getElementById('box01');

	// oBtn.onclick = function(){
	// 	if(oDiv.style.display == 'block' || oDiv.style.display==''){
	// 		oDiv.style.display = 'none';
	// 	}
	// 	else{
	// 		oDiv.style.display = 'block';
	// 	}
		
	// }
	// var oIn1 = document.getElementById('input01');
	// var oIn2 = document.getElementById('input02');
	// var oOut1 = document.getElementById('output');
	// var oBtn = document.getElementById('btn01');
	// oBtn.onclick = function(){
	// 	oOut1.value = parseInt(oIn1.value) * parseInt(oIn2.value);
	// }
		// var iNum1 = 2;
		// var iNum2 = '2';
		// if(iNum1 === iNum2){
		// 	alert('相等');
		// }
		// else{
		// 	alert('不相等');
		// }
		// var iNum1 = 3;
		// switch(iNum1){
		// 	case 1:
		// 	alert('x');
		// 	case 3:
		// 	alert('y');
		// 	break;
		// 	default:
		// 	alert('z');
		// }
		//通过类实例化创建数组
		// var aList01 = new Array(1,'2',3);
		//通过直接量的方式直接创建
		// var aList03 = [1,2,32]
		// aList02.push('6');
		// aList02.pop();
		// aList02.unshift(56);
		// aList02.shift();
		// aList02.reverse();
		// var aRiver = ['asd','ewr','234rew'];
		// aList03.splice(1,1,aRiver);
		// alert(aList03);
		// alert(aList03.indexOf('asd'));
		// alert(aList03.join('-'));
		// var aList = [[1,2,3],[4,5,6,7]];
		// aList.push(1323);
		// alert(aList[1].length);
		
		// for(var i = 0;i < aList.length;i++)
		// {
		// 	if(aList[i] == undefined){
		// 		break;
		// 	}
		// 	alert(aList[i]);
		// }
		// var aList = [1,2,3,4,4,3,2,1,2,3,4,5,6,5,5,3,3,4,2,1];

		// var aList2 = [];

		// for(var i=0;i<aList.length;i++)
		// {
		//     if(aList.indexOf(aList[i])==i)
		//     {
		//         aList2.push(aList[i]);
		//     }
		// }
		// alert(aList2);
		// var aLi = document.getElementsByTagName('li');
		// for(var i=0;i<aLi.length;i++){
		// 	aLi[i].style.listStyle = 'none';
		// 	aLi[i].style.backgroundColor = 'gold';
		// }
		// var oUl = document.getElementById('list1');
		// var aLi2 = oUl.getElementsByTagName('li');
		// for(var i=0;i<aLi2.length;i++){
		// 	aLi2[i].style.listStyle = 'none';
		// 	aLi2[i].style.backgroundColor = 'gold';
		// }
		// var iNum01 = 'abcdef123456edfg';
		// alert(parseInt(iNum01));
		// alert(iNum01.charAt(0));
		// alert(iNum01.substring(1,3));
		// alert(iNum01.toUpperCase());
		// alert(iNum01.toLowerCase());
		// iNum02 = iNum01.split('').reverse().join('');
		// alert(iNum02);
		// var iNum02 = iNum01.substring(iNum01.indexOf('1'),iNum01.indexOf('6')+1);
		// alert(iNum02);
		// function fnMyalert(){
		// 	alert('hello world');
		// }
		// var time1 = setInterval(fnMyalert,1000);
		// clearInterval(time1);
		// clearTimeout(time1);
		// var iLeft = 0;
		// var oDiv = document.getElementById('box01');
		// var timer1 = setInterval(function(){
		// 		iLeft += 1;
		// 		oDiv.style.left = iLeft + 'px';
		// 		if(iLeft > 700){
		// 			clearInterval(timer1);
		// 		}
		// },10);
		// var oTitle = document.getElementById('title');
		// var oDiv = document.getElementById('river');
		// setTimeout(function(){
		// 	oTitle.style.display = 'block';
		// 	oDiv.style.display = 'block';
		// },2000);
// 		window.onload = function(){   
// 		var iLeft = 0;
// 		var iNum = 5;
// 		var oDiv = document.getElementById('box01');
// 		setInterval(function(){
// 				iLeft += iNum;
// 				oDiv.style.left = iLeft + 'px';
// 				if(iLeft > 700){
// 					iNum = -5;
// 				}
// 				else if(iLeft <= 0){
// 					iNum = 5;
// 				}
// 		},10);

// 
// window.onload = function(){
// 	var oDiv =document.getElementById('slide');
// 	var oUl = oDiv.getElementsByTagName('ul')[0];
// 	// alert(oUl.innerHTML);
// 	oUl.innerHTML = oUl.innerHTML + oUl.innerHTML;
// 	var oBtn01 = document.getElementById('btn01');
// 	var oBtn02 = document.getElementById('btn02');
// 	var iLeft = 0;
// 	var iSpace = 2;
// 	function fnmoving(){
// 		//向左移动
// 		iLeft -= iSpace;
// 		oUl.style.left = iLeft + 'px';
// 		if(iLeft < -1000){
// 			iLeft = 0;
// 		}
// 		else if(iLeft>0){
// 			iLeft=-1000;
// 		}
// 		oBtn01.onclick = function(){
// 			iSpace = -2;
// 		}
// 		oBtn02.onclick = function(){
// 			iSpace = 2;
// 		}
// 	}
// 	var iSpeed = iSpace;
// 	var timer = setInterval(fnmoving,20);
// 	oDiv.onmouseover = function(){
// 		iSpace = 0;
// 	}
// 	oDiv.onmouseout = function(){
// 		iSpace = iSpeed;
// 	}

// }
// window.onload = function(){
// 	setInterval(function(){
// 		var oDiv = document.getElementById('div1');
// 		var sNow = new Date();
// 		var iYear = sNow.getFullYear();
// 		var iMonth = sNow.getMonth() + 1;
// 		var iDay = sNow.getDate();
// 		var week = sNow.getDay();
// 	    var hour = sNow.getHours();
// 	    var minute = sNow.getMinutes();
// 	    var second = sNow.getSeconds();
// 	    var str = '当前时间是：'+ iYear + '年'+iMonth+'月'+iDay+'日 '+'星期'+fnToweek(week)+' '+
// 	    fnTotime(hour)+':'+fnTotime(minute)+':'+fnTotime(second);
// 	    oDiv.innerHTML = str;
// 	},1000);

// 	function fnToweek(week){
// 		switch(week){
// 			case 0:
// 			return '日';
// 			case 1:
// 			return '一';
// 			case 2:
// 			return '二';
// 			case 3:
// 			return '三';
// 			case 4:
// 			return '四';
// 			case 5:
// 			return '五';
// 			default:
// 			return '六';
// 		}
// 	}
// 	function fnTotime(time){
// 		if(time<10){
// 			return '0'+time;
// 		}
// 		else
// 		{
// 			return time;
// 		}
// 	}

// }
// window.onload = function(){
// 	var oDiv = document.getElementById('div1');
// 	function fnTime(){
// 	var sNow = new Date();
// 	var sFuture = new Date(2020,3,30,24,0,0);
// 	var iSecond = parseInt((sFuture-sNow)/1000);
// 	var iDay = parseInt(iSecond/86400);
// 	var iHours = parseInt((iSecond%86400)/3600);
// 	var iMinutes =parseInt(((iSecond%86400)%3600)/60);
// 	var iSeconds = iSecond%60;
// 	var sTr = '距离2020年5月1日还剩'+iDay+'天'+iHours+'时'+iMinutes+'分'+
// 	iSeconds+'秒';
// 	oDiv.innerHTML = sTr;
// 	}
// 	fnTime();
// 	setInterval(fnTime,1000);
// }


// window.onload = function(){

	// var oTitle = document.getElementById('title');
	// var oDiv = document.getElementById('river');
	// var oBtn = document.getElementById('btn');
	// var iH3 = document.getElementById('H3');
	// var iTime = 5000;
	// oBtn.onclick = function(){
	// 	oTitle.style.display = 'block';
	// 	oDiv.style.display = 'block';
	// 	setTimeout(function(){
	// 	oTitle.style.display = 'none';
	// 	oDiv.style.display = 'none';
	// },iTime);
	// 	iH3.innerHTML = '5秒后弹窗关闭';

	// }
	// function myalert(){
	// 	alert('hello');
	// }
	// myalert();
	// (function myalert(){
	// 	alert('hell');
	// })();
// 	var oBtn = document.getElementById('btn01');
// 	var sUrl = document.referrer;
// 	oBtn.onclick = function(){
// 		var sTr = window.location.href;
// 		alert(sTr);
// 	}

// 	var iPi = Math.PI;
// 	var iN01 = 10;
// 	var iN02 = 20;
// 	var arr = [];
// 	for(var i=0;i<20;i++){
// 		var iNum = (iN02-iN01+1)*Math.random() + 10;
// 		arr.push(Math.floor(iNum));
// 	}
// 	// console.log(arr);
// 	document.title = arr;
// }



// window.onload = function(){
// 	var oDiv = document.getElementById('div1');
// 	alert(oDiv.innerHTML);
// }

//jquery写法
// $(document).ready(function(){
// 	var $div =  $('#div1');
// 	alert('jquery弹出的'+$div);
// })
// $(function(){
// 	var $div =  $('.list li');
// 	alert('jquery弹出的'+$div);
// })

// $(function(){
	// var $Ul = $('.list li').has('p');
	// var $div = $('#div1');

	// $div.css({'color':'red'})
	// $Ul.css({'color':'pink','background-color':'gold'})

	// var $iList = $('li').filter('.myclass');
	// $iList.css({'background-color':'pink'});
	
// })

// $(function(){
// 	var $Div = $('#box');
// 	var sTr = $Div.css('font-size','30px');
// 	// var oDiv =document.getElementById('box');
// 	// console.log(oDiv.style.fontSize);
// 	//原生js无法获取空行间事件，即未定义css属性
// })

// $(function(){
// 	var $div = $('.box');
// 	$div.addClass('big');
// 	$div.removeClass('big');
// })

// $(function(){
// 	var $btn = $('#btn');
// 	var $div = $(".box");

// 	$btn.click(function(){
// 		// $div.css('color','pink');
// 		// $div.addClass('box1');
// 		// if($('.box').hasClass('col01')){
// 		// 	$('.box').removeClass('col01');
// 		// }
// 		// else{
// 		// 	$('.box').addClass('col01');
// 		// }

// 		//简化写法
// 		$('.box').toggleClass('col01');
// 	})
// })

// $(function(){
// 	// var $li = $('.list li').filter('.myclass');
// 	// alert($li.index());
// 	var $btn = $('.btns input');

// 	var $div = $('.cons div');
// 	$btn.click(function(){
// 		$(this).addClass('current').siblings().removeClass('current');
// 		var iNum = $(this).index()*500;
// 		$div.eq($(this).index()).addClass('action').css('left',iNum).stop().animate({'left':0},1000).
// 		siblings().removeClass('action');

// 	})

// })

// $(function(){
// 	$('#btn').click(function(){
// 		$('.box').slideToggle(1000,'linear',function(){;
// 		});
// 	})
// })
// $(function(){
// 	$('.level1').click(function(){
// 		$(this).next().stop().slideToggle(1000,'linear',function(){;
// 		}).parent().siblings().children('ul').slideUp();
// 	})
// })
// $(function(){
// 	$('#btn').click(function(){
// 		$(".box").animate({width:'+=100px'},100,function(){
// 			$('.box').animate({'height':'400px'},100,function(){
// 				$('.box').stop().animate({'opacity':'-=0.1'},100)
// 			})
// 		});
// })
// })

// $(function(){
// 	// console.log($('.box').width());
// 	// console.log($('.box').innerWidth());
// 	// console.log($('.box').outerWidth());
// 	// console.log($('.box').outerWidth(true));
	
// 	$('.box').click(function(){
// 		var oPos = $('.box').offset();
// 		document.title = oPos.left + '|' + oPos.top;
// 	})
	
// })
// $(function(){
// 	$('.add').click(function(){
// 		var oPos01 = $('.add').offset();
// 		var oPos02 = $('.chart').offset();
// 		var $point = $('.point');
// 		var btnLeft = oPos01.left+parseInt(($('.add').outerWidth())/2)-8;
// 		var btnTop = oPos01.top + parseInt(($('.add').outerHeight())/2)-8;
// 		$point.css({'left':btnLeft,'top':btnTop}).show().animate({'left':oPos02.left+parseInt(($('.chart').outerWidth())/2)-8,'top':
// 			oPos02.top + parseInt(($('.chart').outerHeight())/2)-8},500,function(){
// 				$point.hide(); 
// 				var iNum = $('.chart em').html();
// 				$('.chart em').html(parseInt(iNum)+1);

// 			});
// 	})
// })
// $(function(){
// 	// console.log($(window).width());
// 	// console.log($(window).height());
// 	// console.log($(document).width())
// 	// console.log($(document).height())
// 	var $back = $('.menu_back');
// 	var $totop = $('.totop');

// 	$(window).scroll(function(){
// 		var iNum = $(document).scrollTop();
// 		// console.log(5);
// 		if(iNum > 200){
// 			$('.menu').css({
// 				'position':'fixed',
// 				'left':'50%',
// 				'top':0,
// 				'margin-left':'-480px'
// 				})
// 			$back.show();
// 			$totop.fadeIn(1000).click(function(){
// 		$('html,body').animate({'scrollTop':0})
// 	})
// 		}
// 		else{
// 			$('.menu').css({
// 				'position':'static',
// 				'margin':'0 auto'
// 			})
// 		  $back.hide();
// 		  $totop.fadeOut(1000);
// 		}
// 	})

// })
// $(function(){
// 	var $a = $('.link');
// 	var $img =$('#img01');
// 	console.log($a.prop('class'));
// 	console.log($img.prop('src'));
// 	$a.prop({'href':'http://www.baidu.com','title':'百度网链接'});
// 	console.log($a.html());

// })
// $(function(){
// 	var $li = $('#accordion li');

// 	$li.click(function(){
// 		// alert($(this).html());
// 		$(this).animate({'left':21*$(this).index()});
// 		$(this).prevAll().each(function(){
// 			$(this).animate({'left':21*$(this).index()});
// 		});
// 		$(this).nextAll().each(function(){
// 			$(this).animate({'left':(706-21*(4-$(this).index()))});
// 		});

// 	})
// })

// $(function(){
// 	$("#input01").focus();

// 	$('#input01').blur(function(){
// 		var $val = $(this).val();
// 		alert($val);
// 	});


// })
// $(function(){
// 	// $('.con').mouseover(function(){
// 	// 	alert('移入');
// 	// });
// 	// $('.con').mouseout(function(){
// 	// 	alert('移出');
// 	// });
// 	// $('.con').hover(function(){
// 	// 	alert('123');
// 	// });
// 	// $('#form1').submit(function(){
// 	// 	return false;
// 	// 	// alert('提交');
// 	// })
// 	$(window).resize(function(){
// 		var $w = $(window).width();
// 		document.title = $w;
// 	})
// })

// $(function(){
// 	// $('#btn').bind('click mouseover',function(){
// 	// 	alert('click事件');
// 	// 	$(this).unbind("mouseover");
// 	// })
// 	$('.son').bind('click',function(event){alert(1);
// 		event.stopPropagation();});
// 	$('.grandfather').bind('click',function(event){alert(3);});
// 	$('.father').bind('click',function(event){alert(2);});
// 	$(document).click(function(){
// 		alert('4');
// 	})

// })
// $(function(){
// 	$('#btn').bind('click',function(event){
// 		$('.pop_con').fadeIn();
// 		return false;
// 	});
// 	$(document).click(function(){
// 		$('.pop_con').fadeOut();
// 	})

// 	$('.pop').click(function(){
// 		return false;
// 	})
// 	$('.close').click(function(){
// 		$('.pop_con').fadeOut();
// 	})
// })
// $(function(){
// 	// $('.list li').click(function(){
// 	// 	$(this).css('background-color','pink');
// 	// })
// 	$('.list').delegate('li','click',function(){
// 		$(this).css('background-color','pink');

// 	});
// 	//新建一个li元素赋值给$li变量
// 	var $li = $('<li>9</li>')
// 	$('.list').append($li);


// })

// $(function(){
// 	//$('#div1').html('');

// 	// var $a = $('<a href="#">1</a>');
// 	// var $a2 = $("<a>");
// 	// var $a3 = $("<a>");
// 	// var $a4 = $("<a>");
// 	// $('#div1').append($a);
// 	// $a2.prependTo($("#div1"));
// 	// $a3.insertAfter($('#div1'));
// 	// $a4.insertBefore($('#div1'));
// 	$('#div1').remove();
// })

// $(function(){
	// $('.up').click(function(){
	// 	if($(this).parent().prev().length == 0){
	// 		return '到顶了！';
	// 	}
	// 	else{
	// 		$(this).parent().prev().before($(this).parent());
	// 	}
	// });
	// $('.down').click(function(){
	// 	if($(this).parent().prev().length == 0){
	// 		return '到底了！';
	// 	}
	// 	else{
	// 		$(this).parent().prev().after($(this).parent());
	// 	}
	// });
// 	var $inputtext = $("#txt1");
// 	var $btn = $("#btn1");
// 	var $ul = $("#list");

// 	$btn.click(function(){
// 		//获取输入框中的内容
// 		var $val = $inputtext.val();
// 		if($val == ''){
// 			alert('请输入内容');
// 			return;
// 		}
// 		$ul.append($('<li><span>'+$val+'</span><a href="javascript:;" class="up"> ↑ </a><a href="javascript:;" class="down"> ↓ </a><a href="javascript:;" class="del">删除</a></li>'));
// 		$inputtext.val('');
// 	})

// 	$ul.delegate('a','click',function(){
// 		var $val = $(this).prop('class');
// 		if($val == 'del'){
// 			$(this).parent().remove();
// 		}
// 		else if($val == 'up'){
// 			if($(this).parent().prev().length == 0){
// 				alert('到顶了！');
// 				return;
// 		}
// 		else{
// 			$(this).parent().prev().before($(this).parent());
			
// 		}
// 	}
// 	else{
// 		if($(this).parent().next().length == 0){
// 			alert('到底了！');
// 			return;
// 		}
// 		else{
// 			$(this).parent().prev().after($(this).parent());
// 		}
// 	}
// 	})

// })
// var i = 0;
// $(window).mousewheel(function(event,dat){
// 	i++;
// 	console.log(i);
// })

// $(function(){
// 	var i = 20;
// 	$(window).mousewheel(function(){
// 		i+=i;
// 		$('.box').addClass('moving');
// 		$('.moving').css('transform','rotate('+i+'deg)');
// 	})
	
// })
// $(function(){
// 	var $screen = $(".pages_con");
// 	var $pages = $(".pages");
// 	var $h = $(window).height();
// 	$pages.css({'height':$h});
// 	var $points = $('.points li');
// 	var $nowscreen = 0;
// 	$pages.eq(0).addClass('moving');
// 	var timer = null;

// 	$(window).mousewheel(function(event,dat){
// 		clearTimeout(timer);
// 		timer = setTimeout(function(){
// 			if(dat == -1){
// 			$nowscreen++;
// 			}
// 			else{
// 				$nowscreen--;
// 			}
// 			if($nowscreen<0){
// 				$nowscreen =0;
// 			}
// 			if($nowscreen>$pages.length-1){
// 				$nowscreen=$pages.length-1;
// 			}
// 			$screen.stop().animate({'top':-$h*$nowscreen},300);
// 			$pages.eq($nowscreen).addClass('moving').siblings().removeClass('moving');
// 			$points.eq($nowscreen).addClass('active').siblings().removeClass('active');
		
// 			}
// 		,200)
// 		})
// 	var $ul = $('.points');
// 	$ul.delegate('li','click',function(){
// 		$nowscreen = $(this).index();
// 		$(this).addClass('active').siblings().removeClass('active');
// 		$screen.stop().animate({'top':-$h*$nowscreen},300);
// 		$pages.eq($nowscreen).addClass('moving').siblings().removeClass('moving');
// 	})
// })
// $(function(){

// 	$.ajax({
// 		url:'js/data.js',
// 		type:'get',
// 		dataType:'jsonp',
// 		jsonpCallback:'fnback'
// 	})

// 	.done(function(data){
// 		console.log(data.name);
// 	});
// })
// $(function(){
//     $('#txt01').keyup(function(){
//         var sVal = $(this).val();
//         $.ajax({
//             url:'https://sug.so.360.cn/suggest?',
//             type:'get',
//             dataType:'jsonp',
//             data: {"word": sVal}
//         })
//         .done(function(data){
//             var aData = data.s;
//             $('.list').empty();
//             for(var i=0;i<aData.length;i++)
//             {
//                 var $li = $('<li>'+ aData[i] +'</li>');
//                 $li.appendTo($('.list'));
//             }
//         })        
//     })
// })
// $(function(){
// 	$('.box').draggable({
// 		axis:'x',
// 		containment:'parent',
// 		opacity:0.6,

// 		drag:function(ev,ui){
// 			// console.log(ui);
// 			// document.title = ui.position.left;
// 			var nowflash = ui.position.left;
// 			$('.drgger').css({'width':nowflash});
// 			$('.shownumber').val(parseInt((nowflash/558)*100)+'%');

// 		}
// 	});

// })
//cookie存储
// $.cookie('mycookie','ok',{expires:7,path:'/'});
// var mycookie = $.cookie('mycookie');
// alert(mycookie);
// localStorage.setItem('dat','456');

// sessionStorage.setItem('dat1','123');
//只提示一次弹框

// $(function(){
// 	alert($(".div1").html());
// 	// alert(1);
	
// })

// $(function(){
// 	$("#btn01").click(function(){
// 		//$("#modal01").modal('show');
// 		$("#modal01").modal({
// 			show:true,
// 			backdrop:false
// 		});
// 	})
// 	$("#shutoff").click(function(){
// 		$("#modal01").modal('hide');
// 	})

// })
var re01 = new RegExp('a','i');

var re02 = /a/i;

var re02 = /\d/;
var str01 = 'abcdef123456edfg';
var str02 = 'sdfsdg';
alert(re02.test(str01));
alert(re02.test(str02));