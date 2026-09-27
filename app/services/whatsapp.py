import subprocess


class WhatsappService:

    def __init__(self):

        # ====================================================
        # WHATSAPP CONTACTS
        # ====================================================

        self.contacts = {

            # Replace these later with your real numbers.
            # Use country code without + sign.

            "mama": "923017848720",
            "laiba": "923156774079",

        }

    # ========================================================
    # OPEN WHATSAPP CHAT
    # ========================================================

    def open_chat(self, contact_name):

        contact_name = contact_name.lower().strip()

        # ----------------------------------------------------
        # CHECK CONTACT
        # ----------------------------------------------------

        if contact_name not in self.contacts:

            return (
                f"I don't have a WhatsApp contact saved "
                f"for {contact_name}."
            )

        # ----------------------------------------------------
        # GET PHONE NUMBER
        # ----------------------------------------------------

        phone_number = self.contacts[contact_name]

        # ----------------------------------------------------
        # WHATSAPP WEB CHAT URL
        # ----------------------------------------------------

        url = (
            "https://web.whatsapp.com/send?phone="
            + phone_number
        )

        # ----------------------------------------------------
        # OPEN CHAT
        # ----------------------------------------------------

        try:

            subprocess.Popen(
                [
                    "cmd",
                    "/c",
                    "start",
                    "",
                    url
                ]
            )

            return (
                f"Opening WhatsApp chat with "
                f"{contact_name.title()}."
            )

        except Exception as error:

            print(
                f"WhatsApp chat error: {error}"
            )

            return (
                f"I couldn't open WhatsApp chat "
                f"with {contact_name.title()}."
            )