<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>GTA Burkina - Carte Réelle Population - 24.6M habitants</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{margin:0;background:#0a0a0a;color:#fff;font-family:Arial;overflow:hidden;width:100vw;height:100vh}
#ui{position:fixed;top:0;left:0;right:0;height:48px;background:linear-gradient(#1a1a1a,#000);border-bottom:3px solid #ff7a00;display:flex;align-items:center;justify-content:space-between;padding:0 8px;z-index:100;font-weight:900;font-size:9px}
#main{position:fixed;top:48px;left:0;right:0;bottom:0;display:flex}
#mapArea{flex:1;position:relative;background:#e8dcc0;overflow:hidden}
canvas{width:100%;height:100%;display:block}
#left{width:230px;background:rgba(0,0,0,0.94);border-right:2px solid #00e5ff;padding:6px;overflow-y:auto;font-size:8px;line-height:10px;z-index:20}
#right{width:180px;background:rgba(0,0,0,0.94);border-left:2px solid #ff7a00;padding:6px;font-size:8px;z-index:20}
.region{padding:3px 4px;margin:2px 0;background:#222;border-radius:3px;cursor:pointer;border-left:3px solid #666;display:flex;justify-content:space-between}
.region.active{border-left-color:#ffeb3b;background:#333;color:#ffeb3b}
.region .pop{font-size:7px;color:#aaa}
.city{padding:2px 4px;margin:1px 0;background:#1a1a1a;border-radius:2px;font-size:7px;display:flex;justify-content:space-between;border-left:2px solid #444}
#joy{position:fixed;bottom:12px;right:12px;width:100px;height:100px;background:rgba(255,255,255,0.15);border:3px solid #fff;border-radius:50%;z-index:80}
#stick{position:absolute;left:25px;top:25px;width:50px;height:50px;background:#fff;border-radius:50%}
#btns{position:fixed;bottom:8px;left:50%;transform:translateX(-50%);display:flex;gap:6px;z-index:80}
.btn{width:52px;height:52px;border-radius:50%;border:2px solid #fff;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:6px;font-weight:900;color:#fff;cursor:pointer}
#legend{position:fixed;top:52px;right:190px;background:rgba(0,0,0,0.8);padding:5px 8px;border-radius:6px;font-size:7px;z-index:70;border:1px solid #ff0}
@media(orientation:portrait){body{transform:rotate(90deg);transform-origin:50% 50%;width:100vh;height:100vw;position:fixed;top:50%;left:50%;margin-left:-50vh;margin-top:-50vw}}
</style></head><body>
<div id="ui">
<div>🇧🇫 BURKINA FASO 24.6M hab (2026) | 💰 $<span id="cash">1200</span> | FABRICE | 👥<span id="totalPop">24601700</span> | ⛽<span id="fuel">100</span>%</div>
<div>📍 <span id="currentCity">OUAGADOUGOU 3.2M</span> | 🚓 <span id="wanted">0</span>★</div>
</div>
<div id="legend">
<b>🗺️ DENSITÉ POPULATION</b><br>
<span style="color:#ff0000">■</span> >1000/km² Centre Ouaga<br>
<span style="color:#ff7a00">■</span> 100-200/km² Nord/Centre-Est<br>
<span style="color:#ffeb3b">■</span> 50-100/km² Ouest/Sud<br>
<span style="color:#00ff00">■</span> <50/km² Est/Sahel<br>
<b>RN: Nationale 1-29</b>
</div>
<div id="main">
<div id="left">
<b style="color:#ff7a00">🇧🇫 CARTE RÉELLE 17 RÉGIONS (Réforme 2025 Traoré)</b>
<small style="color:#aaa">Clique région → voyage → population réelle</small>
<div class="region active" onclick="goRegion('Centre')"><span><b>📍 CENTRE</b><br>Ouagadougou<br><small>Capitale</small></span><span class="pop">3.6M hab<br>1308/km²</span></div>
<div class="region" onclick="goRegion('HautsBassins')"><span><b>🌴 HAUTS-BASSINS</b><br>Bobo-Dioulasso</span><span class="pop">2.57M<br>100/km²</span></div>
<div class="region" onclick="goRegion('Nord')"><span><b>🌾 NORD</b><br>Ouahigouya</span><span class="pop">1.93M<br>118/km²</span></div>
<div class="region" onclick="goRegion('CentreOuest')"><span><b>🏫 CENTRE-OUEST</b><br>Koudougou</span><span class="pop">1.86M<br>85/km²</span></div>
<div class="region" onclick="goRegion('Boucle')"><span><b>🌾 BOUCLE MOUHOUN / BANKUI</b><br>Dédougou</span><span class="pop">2.12M<br>61/km²</span></div>
<div class="region" onclick="goRegion('Est')"><span><b>🦁 EST / GOULMOU</b><br>Fada N'Gourma</span><span class="pop">2.24M<br>48/km²</span></div>
<div class="region" onclick="goRegion('CentreNord')"><span><b>⛏️ CENTRE-NORD</b><br>Kaya</span><span class="pop">2.13M<br>108/km²</span></div>
<div class="region" onclick="goRegion('CentreEst')"><span><b>🌽 CENTRE-EST</b><br>Tenkodogo</span><span class="pop">1.78M<br>121/km²</span></div>
<div class="region" onclick="goRegion('Sahel')"><span><b>🐪 SAHEL / LIPTAKO / SOUM</b><br>Dori / Djibo</span><span class="pop">1.22M<br>33/km²</span></div>
<div class="region" onclick="goRegion('Cascades')"><span><b>🍃 CASCADES</b><br>Banfora</span><span class="pop">944K<br>51/km²</span></div>
<div class="region" onclick="goRegion('SudOuest')"><span><b>🏔️ SUD-OUEST</b><br>Gaoua</span><span class="pop">986K<br>60/km²</span></div>
<hr>
<b style="color:#00e5ff">🏙️ VILLES RÉELLES POP 2025 (Worldometer)</b>
<div class="city" onclick="goCity('Ouagadougou')"><span>1. Ouagadougou</span><span>3,206,222 +1.7%</span></div>
<div class="city" onclick="goCity('Bobo')"><span>2. Bobo-Dioulasso</span><span>1,125,023 +1.46%</span></div>
<div class="city" onclick="goCity('Koudougou')"><span>3. Koudougou</span><span>183,409 +2.58%</span></div>
<div class="city" onclick="goCity('Banfora')"><span>4. Banfora</span><span>172,796</span></div>
<div class="city" onclick="goCity('Kaya')"><span>5. Kaya</span><span>143,195 +3.13%</span></div>
<div class="city" onclick="goCity('Fada')"><span>6. Fada N'Gourma</span><span>139,133</span></div>
<div class="city" onclick="goCity('Ouahigouya')"><span>7. Ouahigouya</span><span>128,032</span></div>
<div class="city" onclick="goCity('Tenkodogo')"><span>8. Tenkodogo</span><span>112,011</span></div>
<div class="city" onclick="goCity('Dedougou')"><span>9. Dédougou</span><span>93,251</span></div>
<div class="city" onclick="goCity('Dori')"><span>13. Dori (Sahel)</span><span>69,583</span></div>
<hr>
<b>📋 MISSIONS NATIONALES</b>
<div class="city" onclick="startMission('OuagaBobo')" style="border-left-color:#ff0000"><span>🚛 RN1: Ouaga → Bobo 360km<br>Or + coton</span><span>+2500$</span></div>
<div class="city" onclick="startMission('Sahel')" style="border-left-color:#ffeb3b"><span>🐪 Sahel: Dori → Djibo<br>Aide humanitaire</span><span>+1800$</span></div>
<div class="city" onclick="startMission('Est')" style="border-left-color:#00ff00"><span>🦁 Est: Fada → Parc W<br>Touristes</span><span>+2000$</span></div>
</div>
<div id="mapArea"><canvas id="c"></canvas></div>
<div id="right">
<b style="color:#ffeb3b">👥 POPULATION DANS TA ZONE</b>
<div id="popInfo" style="background:#222;padding:4px;border-radius:4px;margin:4px 0">Ouagadougou:<br><b>3,206,222 hab</b><br>Densité: 6464/km²<br>Croissance: +1.7%/an<br>Ethnie: Mossi 52%<br>Religion: Musulman 63%<br>34.5% urbain</div>
<div id="peopleList" style="max-height:100px;overflow-y:auto;font-size:7px"></div>
<hr>
<b>🚗 VÉHICULES ADAPTÉS TERRAIN</b>
<div class="city" onclick="setVeh('103')" style="background:#2a3a2a;border-color:#0f0"><span>🛵 103 SP - Ville dense</span><span>GO</span></div>
<div class="city" onclick="setVeh('hilux')"><span>🛻 Hilux - Brousse Sahel</span><span>6000$</span></div>
<div class="city" onclick="setVeh('sotraco')"><span>🚌 SOTRACO - Transport pop</span><span>3500$</span></div>
<div class="city" onclick="setVeh('taxi')"><span>🚕 Taxi Vert - Ouaga/Bobo</span><span>2000$</span></div>
<hr>
<b>⛽ CARBURANT & DISTANCE</b>
<div id="fuelInfo" style="background:#331;padding:3px;border-radius:3px">Ouaga → Bobo: 360km<br>Carburant: -15%<br>Temps: 5h<br>Population traversée: ~4M</div>
<hr>
<div id="policeMsg" style="background:#300;padding:3px;border-radius:3px;font-size:7px">Calme - Harmattan 32°C</div>
</div>
</div>
<div id="joy"><div id="stick"></div></div>
<div id="btns">
<div class="btn" id="sprint" style="background:#0d47a1">🏃<br>SPRINT</div>
<div class="btn" id="mapBtn" style="background:#ff7a00">🗺️<br>CARTE<br>PAYS</div>
<div class="btn" id="inter" style="background:#2e7d32">🖐️<br>PARLER<br>Gens</div>
<div class="btn" id="shoot" style="background:#b71c1c">🔫<br>TIRER</div>
</div>
<script>
const canvas=document.getElementById('c'),ctx=canvas.getContext('2d');
function resize(){canvas.width=canvas.parentElement.clientWidth*2;canvas.height=canvas.parentElement.clientHeight*2;}resize();window.addEventListener('resize',resize);
let cash=1200,fuel=100,wanted=0,currentRegion='Centre',currentCity='Ouagadougou';
let player={x:400,y:300,angle:0,speed:0,type:'103'};
let npcs=[],bullets=[];
let cities={
 'Ouagadougou':{x:400,y:300,pop:3206222,density:6464,growth:1.7,region:'Centre',ethnie:'Mossi 52%',color:'#ff0000',npcCount:25},
 'Bobo':{x:150,y:350,pop:1125023,density:6618,growth:1.46,region:'HautsBassins',ethnie:'Bobo 4.9%',color:'#ff7a00',npcCount:18},
 'Koudougou':{x:300,y:320,pop:183409,density:3596,growth:2.58,region:'CentreOuest',ethnie:'Gurunsi',color:'#ffeb3b',npcCount:10},
 'Banfora':{x:100,y:400,pop:172796,density:5574,growth:1.79,region:'Cascades',ethnie:'Senufo 4.5%',color:'#00ff00',npcCount:8},
 'Kaya':{x:450,y:200,pop:143195,density:4091,growth:3.13,region:'CentreNord',ethnie:'Mossi',color:'#00e5ff',npcCount:7},
 'Fada':{x:650,y:350,pop:139133,density:4348,growth:1.59,region:'Est',ethnie:'Gurma 7%',color:'#9c27b0',npcCount:6},
 'Ouahigouya':{x:300,y:120,pop:128032,density:4001,growth:0.73,region:'Nord',ethnie:'Mossi',color:'#e91e63',npcCount:6},
 'Tenkodogo':{x:550,y:380,pop:112011,density:4480,growth:1.65,region:'CentreEst',ethnie:'Bissa 3.7%',color:'#795548',npcCount:5},
 'Dedougou':{x:250,y:250,pop:93251,density:4239,growth:2.01,region:'Boucle',ethnie:'Bwaba',color:'#607d8b',npcCount:4},
 'Dori':{x:600,y:80,pop:69583,density:6326,growth:2.01,region:'Sahel',ethnie:'Peulh 8.4% + Touareg',color:'#ffcc00',npcCount:3}
};
function createPeopleForCity(cityName){
 let city=cities[cityName]||cities['Ouagadougou'];
 npcs=[];
 for(let i=0;i<city.npcCount;i++){
  npcs.push({x:city.x-100+Math.random()*200,y:city.y-80+Math.random()*160,name:cityName+' habitant '+i,type:'citizen',color:city.color,vx:(Math.random()-0.5)*0.6,vy:(Math.random()-0.5)*0.6,state:'walk',pop:city.pop,size:8+Math.random()*6});
 }
 document.getElementById('popInfo').innerHTML=`<b>${cityName}</b><br><b>${city.pop.toLocaleString()} hab</b><br>Densité: ${city.density}/km²<br>Croissance: +${city.growth}%/an<br>Région: ${city.region}<br>Ethnie dom: ${city.ethnie}<br>NPCs GTA: ${city.npcCount} (selon densité)`;
 updatePeopleList();
}
createPeopleForCity('Ouagadougou');
function updatePeopleList(){
 let html='';
 npcs.slice(0,8).forEach(p=>{html+=`<div style="padding:1px;background:#222;margin:1px;border-radius:2px">👤 ${p.name} - ${p.state}</div>`});
 document.getElementById('peopleList').innerHTML=html;
}
function goRegion(r){
 currentRegion=r;
 document.querySelectorAll('.region').forEach(e=>e.classList.remove('active'));
 event.target.closest('.region').classList.add('active');
 let cityMap={'Centre':'Ouagadougou','HautsBassins':'Bobo','Nord':'Ouahigouya','CentreOuest':'Koudougou','Boucle':'Dedougou','Est':'Fada','CentreNord':'Kaya','CentreEst':'Tenkodogo','Sahel':'Dori','Cascades':'Banfora','SudOuest':'Gaoua'};
 let target=cityMap[r]||'Ouagadougou';
 goCity(target);
 fuel=Math.max(0,fuel-10); document.getElementById('fuel').innerText=fuel;
}
function goCity(name){
 currentCity=name;
 let city=cities[name]; if(!city) return;
 player.x=city.x; player.y=city.y;
 document.getElementById('currentCity').innerText=name.toUpperCase()+' '+ (city.pop/1000).toFixed(0)+'K';
 createPeopleForCity(name);
 updatePolice("Arrivé à "+name+" - Population "+city.pop.toLocaleString()+" - Densité "+city.density+"/km²");
}
function setVeh(t){player.type=t; updatePolice("Véhicule "+t+" - Adapté à "+currentRegion);}
function startMission(type){
 if(type==='OuagaBobo'){updatePolice("Mission NATIONALE: Ouaga 3.2M → Bobo 1.1M - 360km - Transporte or + coton - Population traversée 4.7M - RN1"); fuel-=15; wanted=1;}
 else if(type==='Sahel'){updatePolice("Mission SAHEL: Dori 69K → Djibo 59K - Zone sahélienne 33/km² - Aide humanitaire - Attention insécurité"); fuel-=12; wanted=2;}
 else if(type==='Est'){updatePolice("Mission EST: Fada → Parc W UNESCO - Faune lions éléphants - Touristes - 48/km²"); fuel-=10;}
 document.getElementById('fuel').innerText=fuel;
}
function updatePolice(msg){document.getElementById('policeMsg').innerText=msg;document.getElementById('wanted').innerText=wanted;}
function drawBurkinaMap(){
 ctx.fillStyle='#e8dcc0';ctx.fillRect(0,0,canvas.width,canvas.height);
 ctx.fillStyle='rgba(255,235,180,0.6)';ctx.strokeStyle='#8d6e63';ctx.lineWidth=3;
 ctx.beginPath();
 let pts=[[350,80],[500,70],[620,100],[680,200],[660,380],[600,480],[450,500],[300,480],[150,420],[120,250],[200,120]];
 ctx.moveTo(pts[0][0]*2,pts[0][1]*2);
 for(let i=1;i<pts.length;i++) ctx.lineTo(pts[i][0]*2,pts[i][1]*2);
 ctx.closePath();ctx.fill();ctx.stroke();
 ctx.strokeStyle='#2196f3';ctx.lineWidth=2;ctx.setLineDash([8,4]);
 ctx.beginPath();ctx.moveTo(200*2,300*2);ctx.quadraticCurveTo(400*2,280*2,600*2,150*2);ctx.stroke();
 ctx.beginPath();ctx.moveTo(400*2,100*2);ctx.quadraticCurveTo(420*2,250*2,500*2,450*2);ctx.stroke();
 ctx.setLineDash([]);
 for(let key in cities){
  let c=cities[key];
  let densityColor= c.density>1000?'#ff0000':c.density>100?'#ff7a00':c.density>50?'#ffeb3b':'#00ff00';
  ctx.fillStyle=densityColor;ctx.globalAlpha=0.3;
  ctx.beginPath();ctx.arc(c.x*2,c.y*2,20+c.pop/80000,0,6.28);ctx.fill();ctx.globalAlpha=1;
  ctx.fillStyle=c.color;ctx.beginPath();ctx.arc(c.x*2,c.y*2,6,0,6.28);ctx.fill();
  ctx.fillStyle='#000';ctx.font='bold 9px Arial';ctx.fillText(key+' '+ (c.pop/1000).toFixed(0)+'K',c.x*2+8,c.y*2-8);
  ctx.font='7px Arial';ctx.fillText(c.density+'/km²',c.x*2+8,c.y*2);
 }
 ctx.strokeStyle='#555';ctx.lineWidth=2;
 ctx.beginPath();ctx.moveTo(cities['Ouagadougou'].x*2,cities['Ouagadougou'].y*2);ctx.lineTo(cities['Bobo'].x*2,cities['Bobo'].y*2);ctx.stroke();
 ctx.beginPath();ctx.moveTo(cities['Ouagadougou'].x*2,cities['Ouagadougou'].y*2);ctx.lineTo(cities['Ouahigouya'].x*2,cities['Ouahigouya'].y*2);ctx.stroke();
 ctx.beginPath();ctx.moveTo(cities['Ouagadougou'].x*2,cities['Ouagadougou'].y*2);ctx.lineTo(cities['Fada'].x*2,cities['Fada'].y*2);ctx.stroke();
 npcs.forEach(p=>{
  p.x+=p.vx; p.y+=p.vy;
  if(p.x<20||p.x>780) p.vx*=-1;
  if(p.y<20||p.y>500) p.vy*=-1;
  ctx.fillStyle=p.color;ctx.beginPath();ctx.arc(p.x*2,p.y*2,4,0,6.28);ctx.fill();
  ctx.fillStyle='#ffdbac';ctx.beginPath();ctx.arc(p.x*2,p.y*2-6,3,0,6.28);ctx.fill();
 });
 ctx.save();ctx.translate(player.x*2,player.y*2);ctx.rotate(player.angle);
 ctx.fillStyle='#2196f3';ctx.fillRect(-12,-6,24,12);
 ctx.fillStyle='#ffdbac';ctx.beginPath();ctx.arc(0,-10,5,0,6.28);ctx.fill();
 ctx.restore();
 ctx.fillStyle='rgba(0,0,0,0.7)';ctx.fillRect(10,10,200,70);
 ctx.fillStyle='#fff';ctx.font='bold 10px Arial';ctx.fillText('BURKINA FASO 274,200 km²',15,22);
 ctx.font='8px Arial';ctx.fillText('Population 2026: 24,601,700 hab',15,34);
 ctx.fillText('Densité: 90/km² | Urbain: 34.5%',15,44);
 ctx.fillText('Mossi 52% | Musulman 63.2%',15,54);
 ctx.fillText('Fleuves: Mouhoun, Nakanbé, Nazinon',15,64);
 ctx.fillText('Réforme 2025: 13→17 régions (Traoré)',15,74);
 requestAnimationFrame(drawBurkinaMap);
}
drawBurkinaMap();
let joy={x:0,y:0};const base=document.getElementById('joy'),stick=document.getElementById('stick');
function handle(e){let r=base.getBoundingClientRect();let cx=r.left+r.width/2,cy=r.top+r.height/2;let x=(e.touches?e.touches[0].clientX:e.clientX)-cx;let y=(e.touches?e.touches[0].clientY:e.clientY)-cy;let d=Math.min(35,Math.hypot(x,y));let a=Math.atan2(y,x);joy.x=Math.cos(a)*d/35;joy.y=Math.sin(a)*d/35;stick.style.left=25+joy.x*24+'px';stick.style.top=25+joy.y*24+'px';player.angle=a;if(d>8)player.speed=3;}
base.addEventListener('touchstart',e=>{e.preventDefault();handle(e);});base.addEventListener('touchmove',e=>{e.preventDefault();handle(e);},{passive:false});base.addEventListener('touchend',()=>{joy.x=0;joy.y=0;stick.style.left='25px';stick.style.top='25px';});
document.getElementById('sprint').addEventListener('touchstart',()=>{player.speed+=5;fuel=Math.max(0,fuel-0.5);document.getElementById('fuel').innerText=Math.floor(fuel);});
document.getElementById('mapBtn').addEventListener('touchstart',()=>{updatePolice("Carte nationale: 17 régions, 47 provinces, 351 communes - Pop 24.6M - Clique ville pour voyager");});
document.getElementById('inter').addEventListener('touchstart',()=>{let near=npcs.find(p=>Math.hypot(player.x-p.x,player.y-p.y)<20);if(near){updatePolice(near.name+": "+currentCity+" a "+cities[currentCity].pop.toLocaleString()+" habitants! Densité "+cities[currentCity].density+"/km²");}else{updatePolice("Info: "+currentCity+" - Ethnie "+cities[currentCity].ethnie);}});
document.getElementById('shoot').addEventListener('touchstart',()=>{bullets.push({x:player.x*2,y:player.y*2,a:player.angle});if(wanted<4){wanted++;updatePolice("Tir - Foule fuit - Police "+currentRegion);npcs.forEach(n=>n.state='flee');}});
try{screen.orientation.lock('landscape');}catch(e){}
</script>
</body></html>
