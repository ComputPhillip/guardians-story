// usage: node run.js map.html scenario.json out.json
const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{
 const [map,scn,out]=process.argv.slice(2); const acts=scn?JSON.parse(fs.readFileSync(scn)):[];
 const b=await chromium.launch(); const p=await b.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(String(e)));
 await p.addInitScript(a=>{window.__acts=a},acts);
 await p.goto('file://'+map); await p.waitForFunction(()=>window.__map&&window.__map.E,null,{timeout:240000});
 const r=await p.evaluate(()=>{const M=window.__map,E=M.E,W=M.W;
  const towns=W.towns.map(t=>t.name);
  const ev={}; E.events.forEach((day,d)=>{ (Array.isArray(day)?day:[day]).forEach(x=>{ if(!x||!x.kind) return; (ev[x.kind]=ev[x.kind]||[]).push([d,x.text]); }); });
  const states=E.state.map(d=>Array.from(d));
  const hamSt=E.ham.map(d=>d.map(h=>h[0]));
  return {towns,STATES:M.STATES,errs:[],days:E.state.length,states,hamSt,campMen:E.campMen,adv:E.adv,tpop:E.tpop,leak:E.leak.map(d=>Object.values(d).reduce((a,b)=>a+b,0)),
   packs:E.packs.length,raids:E.raids.length,events:ev,legend:E.legend,acts:E.acts,player:{rep:E.player.rep,bounty:E.player.bounty,titles:E.player.titles,renown:E.player.renown,fame:E.player.fame,coin:E.player.coin,log:E.player.log},
   lord:E.lord,slavers:E.slavers,school:{name:E.school.name,students:E.school.students,graduated:E.school.graduated},seasonLog:E.seasonLog,retired:E.retired.length,recruited:E.recruited.length,
   playerDay:E.playerDay[E.playerDay.length-1], factions:W.factions?W.factions.map(f=>[f.name,f.camps&&f.camps.length]):null};});
 r.errs=errs; fs.writeFileSync(out,JSON.stringify(r)); console.log('ok',out,'days',r.days,'errs',errs.length); await b.close();
})();
