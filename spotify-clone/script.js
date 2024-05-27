let currentSong = new Audio();
let songs=[];
function convertSecondsToMinSec(seconds) {
    seconds = Math.floor(seconds); // Round down to nearest whole number
    let minutes = Math.floor(seconds / 60);
    let remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
}

async function getSongs() {
    
    let a=await fetch("songs/")
    let response= await a.text();
    console.log(response)
    
    let div=document.createElement("div")
    div.innerHTML=response
    //document.body.appendChild(div);
    let as=div.getElementsByTagName("a")
    //let songs=[]
    for (let index = 0; index < as.length; index++) {
        const element = as[index];
        if (element.href.endsWith(".mp3")) {
            songs.push(element.href.split("/songs/")[1])
        }
        
        
    }
    return songs;
} 

function playMusic(song) {
    currentSong.src="/songs/"+song;
    currentSong.play()
    play.src="pause.svg"
    document.querySelector(".songinfo").innerHTML=song
    
   // document.querySelector(".songtime").innerHTML=convertSecondsToMinSec(currentSong.currentTime)+"/"+convertSecondsToMinSec(currentSong.duration)

}
/* 
async function getSongs() {
    let a = await fetch("http://127.0.0.1:3000/songs/");
    let response = await a.text();
    
    let div = document.createElement("div");
    div.innerHTML = response;
    
    let as = div.querySelectorAll("a"); // Use querySelectorAll on the div
    let songs = [];
    for (let index = 0; index < as.length; index++) {
        const element = as[index];
        if (element.href.endsWith(".mp3")) {
            songs.push(element.href.split("/songs/")[1]);
        }
    }
    return songs;
} */

async function main() {
    let songs=await getSongs()

    //console.log(songs);
    let songUL=document.querySelector(".songlist").getElementsByTagName("ol")[0];
    for (const song of songs) {
        songUL.innerHTML=songUL.innerHTML+`<li> ${song} </li>`
    }
    Array.from(document.querySelector(".songlist").getElementsByTagName("li")).forEach(e=>{
        e.addEventListener("click",ele=>{
            console.log(e.innerHTML.trim());
            playMusic(e.innerHTML.trim());
        })
    })
    play.addEventListener("click",()=>{
        if (currentSong.paused) {
            currentSong.play()
            play.src="pause.svg"
        }else{
            currentSong.pause()
            play.src="play.svg"
        }
    })

    currentSong.addEventListener("timeupdate",()=>{
        document.querySelector(".songtime").innerHTML=convertSecondsToMinSec(currentSong.currentTime)+"/"+convertSecondsToMinSec(currentSong.duration);
        document.querySelector(".circle").style.left=(currentSong.currentTime/currentSong.duration)*100 +"%";
    })

    document.querySelector(".seekbar").addEventListener("click",e=>{
        let percent=(e.offsetX/e.target.getBoundingClientRect().width)*100;
        document.querySelector(".circle").style.left=percent+"%";
        currentSong.currentTime=((currentSong.duration)*percent)/100;
    })

    document.querySelector(".hamburger").addEventListener("click",()=>{
        document.querySelector(".left").style.left=0;
    })

    document.querySelector(".cross").addEventListener("click",()=>{
        document.querySelector(".left").style.left="-100%";
    })

    prev.addEventListener("click",()=>{
        let index=songs.indexOf(currentSong.src.split("/songs/")[1]);
        if (index>0) {
            playMusic(songs[index-1]);
        }
        
    })

    next.addEventListener("click",()=>{
        let index=songs.indexOf(currentSong.src.split("/songs/")[1]);
        if (index<(songs.length)-1) {
            playMusic(songs[index+1]);
        }
    })
    console.log(currentSong.src);
}
main()
