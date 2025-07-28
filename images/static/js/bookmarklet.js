const siteUrl = '//127.0.0.1:8000/';
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250;
const minHeight = 250;

// load css
const head = document.getElementsByTagName('head')[0]
const link = document.createElement('link')
link.rel = 'stylesheet'
link.type = 'text/css'
link.href = styleUrl + '?r=' + Math.floor(Math.random() * 9999999999999999)
head.appendChild(link)

// load HTML
const body = document.getElementsByTagName('body')[0]
boxHtml = `
    <div id='bookmarklet'>
        <a href='#' id = 'close'>&times;</a>
        <h1>Select an image to bookmark:</h1>
        <div class = 'images'></div>
    </div> `;
body.innerHTML += boxHtml;

function bookmarkletLaunch() {
    bookmarklet = document.getElementById('bookmarklet');
    const imagesFound = bookmarklet.queryselector('.images') // clear images found
    imagesFound.innerHTML = '' //display bookmarklet
    bookmarklet.style.display = 'block'
    //close event
    bookmarklet.queryselector('#close').addEventListener('click', function () {
        bookmarklet.style.display = 'none'

    });

}
//launch the bookmarklet
bookmarkletLaunch();