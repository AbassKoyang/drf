const contentContainer = document.getElementById('content-container');
const loginForm = document.getElementById('login-form');
const logoutButton = document.getElementById('lg-btn');
const baseEndpoint = 'http://localhost:8000/api'
if(loginForm){
    loginForm.addEventListener('submit', async (event) => {
        console.log(event);
        event.preventDefault();
        const loginEndpoint = `${baseEndpoint}/token/`;
        const formData = new FormData(loginForm);
        const body = JSON.stringify(Object.fromEntries(formData))
        console.log(body)
        const response = await fetch(loginEndpoint, {
            method: 'POST',
            headers: {
                "Content-Type": 'application/json',
            },
            body
        })
        const data = await response.json();
        console.log(data);
        handleAuthData(data, getProductList);
    })
}
if(logoutButton){
    logoutButton.addEventListener('click', () => {
        localStorage.removeItem("access")
        localStorage.removeItem("refresh")
    })
}

const handleAuthData = (data, callback) => {
    localStorage.setItem('access', data.access)
    localStorage.setItem('refresh', data.refresh)
    if (callback) {
        callback()
    }
}

const getProductList =  async () => {
    const endpoint = `${baseEndpoint}/products/`;
    const options = {
        method: "GET",
        headers: {
            "content-type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}`
        }
    }
   
    try {
        const response = await authFetch(endpoint, options)
        const data = await response.json();
        console.log(data);
        if(data) writeToContainer(data)
    } catch (error) {
        console.error('failed to get product list', error)
    }
}

const writeToContainer = (data) => {
    if (contentContainer){
        contentContainer.innerHTML = `<pre>${JSON.stringify(data, null, 4)}</pre>`
    }
}

const checkAuth = async () => {
    const accessToken = localStorage.getItem('access')
    if(!accessToken){
        if (contentContainer){
            contentContainer.innerHTML = `<pre>You are currently Logged out</pre>`
        }
    }
}

const refreshToken = async () => {
    const endpoint = `${baseEndpoint}/token/refresh/`;
    const rt = localStorage.getItem('refresh')
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                refresh: rt
            })
        })
    
        const data = await response.json()
        if(data.access){
            localStorage.setItem('access', data.access)
        }
        console.log('Token refreshed')
    } catch (error) {
        console.error('Error while refreshing token: ', error)
    }
}

const authFetch = async (url, options={}) => {
    let res = await fetch(url, {...options,
        headers: {
            ...options.headers,
            Authorization: `Bearer ${localStorage.getItem("access")}`,
        }}
    )

    if(res.status === 403 || res.status === 401){
        await refreshToken()
        res = res = await fetch(url, {...options,
            headers: {
                ...options.headers,
                Authorization: `Bearer ${localStorage.getItem("access")}`,
            }}
        )
    }

    return res;
}

checkAuth()
if(localStorage.getItem('access')){
    getProductList()
}