import{_ as t}from"./Apps.c362a520.js";import{h as o}from"./http.19277431.js";import{d as l,I as p,o as n,h as c,a,J as r,w as i,q as f,F as d,s as u}from"./vendor.63914961.js";const _=u("h1",null,"Liste des applications disponibles ",-1),k=l({setup(m){console.log("http://185.189.156.201:9081");const s=p({allApps:{}});return o.get("allStack").then(e=>{s.allApps=e.data.stacks,console.log(s.allApps)},e=>{console.log(e)}),(e,h)=>(n(),c(d,null,[a(r,{align:"center",justify:"center"},{default:i(()=>[_]),_:1}),a(t,{apps:f(s).allApps,view:!1,update:!1,config:!0,info:!0,delete:!1},null,8,["apps"])],64))}});export{k as default};