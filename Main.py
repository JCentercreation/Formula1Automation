import RefreshRunning
import WebScraping
import EmailDelivery

URL = RefreshRunning.DefineEvent()
RefreshRunning.CheckAvailability(URL)
WebScraping.webscraping(URL)
EmailDelivery.emaildelivery()