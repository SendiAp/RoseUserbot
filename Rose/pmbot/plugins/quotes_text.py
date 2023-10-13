import random

QUOTE = {'<i> **“You only live once, but if you do it right, once is enough.”**\n\n — Mae West</i>',



         '<i>**“Many of life’s failures are people who did not realize how close they were to success when they gave up.”**\n\n– Thomas A. Edison</i>',



         '<i>**“Money and success don’t change people; they merely amplify what is already there.”**\n\n — Will Smith</i>',



         '<i>**"Your time is limited, so don’t waste it living someone else’s life. Don’t be trapped by dogma – which is living with the results of other people’s thinking.”**\n\n – Steve Jobs</i>',



         '<i>**“In order to write about life first you must live it.”**\n\n– Ernest Hemingway</i>',



         '<i>**“Turn your wounds into wisdom.”** \n\n— Oprah Winfrey</i>'}



length = 1



GENERATED_QUOTE = "".join(random.sample(QUOTE, length))
