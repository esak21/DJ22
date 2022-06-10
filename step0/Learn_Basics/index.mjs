import os from 'os'
import express from 'express'
import fetch from 'node-fetch'

const app = express()
const PORT=3000

app.get('/' , (req, res) => {
    const helloMessage = `VERSION2::Hello from the ${os.hostname()}`
    console.log(helloMessage)
    res.send(helloMessage)
})

app.get("/nginx", async (req, res) => {
    const url ="http://nginx"
    const response = await fetch(url)
    const body = await response.text()
    res.send(body)
})
app.listen(PORT, () => {
    console.log(`Webserver is listening at the PORT ${PORT}`)
})