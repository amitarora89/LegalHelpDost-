from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.scrollview import MDScrollView
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty

# --- KV LANGUAGE LAYOUT ---
KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex

# 1. Custom Dashboard Card Design
<HomeScreenCard>:
    orientation: "vertical"
    padding: "10dp"
    spacing: "5dp"
    radius: [15,]
    elevation: 4
    ripple_behavior: True
    md_bg_color: get_color_from_hex("#ffffff")
    on_release: app.change_screen(root.dest_screen)
    size_hint: 1, None
    height: "130dp"
    
    MDIcon:
        icon: root.icon
        halign: "center"
        font_size: "38sp"
        theme_text_color: "Custom"
        text_color: get_color_from_hex("#1a365d")
        size_hint_y: None
        height: "45dp"
    
    MDLabel:
        text: root.text
        halign: "center"
        bold: True
        font_style: "Subtitle2"
        theme_text_color: "Custom"
        text_color: get_color_from_hex("#1a365d")
        size_hint_y: None
        height: self.texture_size[1]

# 2. Responsive Text Field (Fits Mobile Screen)
<CommonTextField@MDTextField>:
    mode: "rectangle"
    size_hint_x: 1
    pos_hint: {"center_x": 0.5}

# --- SCREEN MANAGER ---
MDScreenManager:
    id: screen_manager
    
    MainScreen:
        name: "main"
    
    GSTScreen:
        name: "gst"
    
    TaxScreen:
        name: "tax"
    
    PropertyScreen:
        name: "property"
        
    ChallanScreen:
        name: "challan"
    
    CounselScreen:
        name: "counsel"

    FeedbackScreen:
        name: "feedback"

# --- 1. MAIN SCREEN ---
<MainScreen>:
    name: "main"
    
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "LegalHelpDost"
            elevation: 4
            md_bg_color: get_color_from_hex("#1a365d")
            specific_text_color: 1, 1, 1, 1
            right_action_items: [["dots-vertical", lambda x: app.show_menu()]]
        
        MDScrollView:
            do_scroll_x: False
            
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "15dp"
                spacing: "20dp"
                
                # Welcome Card
                MDCard:
                    orientation: "vertical"
                    size_hint_x: 0.95
                    size_hint_y: None
                    height: "110dp"
                    pos_hint: {"center_x": 0.5}
                    radius: [20,]
                    md_bg_color: get_color_from_hex("#2d6ae3")
                    padding: "15dp"
                    elevation: 4
                    
                    MDLabel:
                        text: "Welcome User!"
                        font_style: "H6"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        bold: True
                        
                    MDLabel:
                        text: "Complete Legal Solutions"
                        font_style: "Body1"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 0.9

                MDLabel:
                    text: "Our Services"
                    font_style: "H6"
                    bold: True
                    adaptive_height: True
                    padding_x: "10dp"
                    color: get_color_from_hex("#333333")

                # Services Grid (2 Columns)
                MDGridLayout:
                    cols: 2
                    adaptive_height: True
                    spacing: "15dp"
                    padding: "5dp"
                    size_hint_x: 1
                    
                    HomeScreenCard:
                        icon: "file-document-outline"
                        text: "GST Filing"
                        dest_screen: "gst"

                    HomeScreenCard:
                        icon: "calculator-variant"
                        text: "ITR Filing"
                        dest_screen: "tax"
                        
                    HomeScreenCard:
                        icon: "home-city-outline"
                        text: "Property Papers"
                        dest_screen: "property"
                        
                    HomeScreenCard:
                        icon: "motorbike"
                        text: "Pay Challan"
                        dest_screen: "challan"
                        
                    HomeScreenCard:
                        icon: "gavel"
                        text: "Lawyer Help"
                        dest_screen: "counsel"

                    HomeScreenCard:
                        icon: "message-draw"
                        text: "App Feedback"
                        dest_screen: "feedback"

# --- 2. GST SCREEN ---
<GSTScreen>:
    name: "gst"
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "GST Services"
            left_action_items: [["arrow-left", lambda x: app.change_screen('main')]]
            md_bg_color: get_color_from_hex("#1976D2")
            elevation: 4
            
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "20dp"
                spacing: "20dp"
                
                MDLabel:
                    text: "File GST Returns"
                    halign: "center"
                    font_style: "H5"
                    bold: True
                    adaptive_height: True
                
                MDCard:
                    orientation: "vertical"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    padding: "15dp"
                    spacing: "15dp"
                    radius: [15,]
                    adaptive_height: True
                    elevation: 3
                    
                    CommonTextField:
                        hint_text: "Business Name"
                    
                    CommonTextField:
                        hint_text: "GST Number (Optional)"
                        
                    CommonTextField:
                        hint_text: "Phone Number"
                        input_filter: "int"
                        
                    MDRaisedButton:
                        text: "Submit Request"
                        size_hint_x: 1
                        md_bg_color: get_color_from_hex("#1976D2")
                        on_release: app.show_success("Request Sent! Expert will call you.")

# --- 3. INCOME TAX SCREEN ---
<TaxScreen>:
    name: "tax"
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "ITR Filing"
            left_action_items: [["arrow-left", lambda x: app.change_screen('main')]]
            md_bg_color: get_color_from_hex("#F57C00")
            elevation: 4
            
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "20dp"
                spacing: "20dp"
                
                MDLabel:
                    text: "File ITR Online"
                    halign: "center"
                    font_style: "H5"
                    bold: True
                    adaptive_height: True
                
                MDCard:
                    orientation: "vertical"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    padding: "15dp"
                    spacing: "15dp"
                    radius: [15,]
                    adaptive_height: True
                    elevation: 3
                    
                    CommonTextField:
                        hint_text: "Full Name"
                    
                    CommonTextField:
                        hint_text: "Annual Income (Approx)"
                        
                    CommonTextField:
                        hint_text: "Mobile Number"
                        input_filter: "int"
                        
                    MDRaisedButton:
                        text: "Request Callback"
                        size_hint_x: 1
                        md_bg_color: get_color_from_hex("#F57C00")
                        on_release: app.show_success("We will call you for ITR filing.")

# --- 4. PROPERTY SCREEN ---
<PropertyScreen>:
    name: "property"
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "Property Papers"
            left_action_items: [["arrow-left", lambda x: app.change_screen('main')]]
            md_bg_color: get_color_from_hex("#388E3C")
            elevation: 4
            
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "20dp"
                spacing: "20dp"
                
                MDLabel:
                    text: "Draft Legal Documents"
                    halign: "center"
                    font_style: "H5"
                    bold: True
                    adaptive_height: True
                
                MDCard:
                    orientation: "vertical"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    padding: "15dp"
                    spacing: "15dp"
                    radius: [15,]
                    adaptive_height: True
                    elevation: 3
                    
                    MDLabel:
                        text: "Select Document Type:"
                        adaptive_height: True
                        bold: True
                        
                    MDFillRoundFlatButton:
                        text: "Rent Agreement"
                        size_hint_x: 1
                        on_release: app.show_success("Rent Agreement Selected")
                        
                    MDFillRoundFlatButton:
                        text: "Sale Deed (Registry)"
                        size_hint_x: 1
                        md_bg_color: get_color_from_hex("#5D4037")
                        on_release: app.show_success("Sale Deed Selected")
                        
                    CommonTextField:
                        hint_text: "Your Name"
                    
                    CommonTextField:
                        hint_text: "Mobile Number"
                        input_filter: "int"
                        
                    MDRaisedButton:
                        text: "Send Request"
                        size_hint_x: 1
                        md_bg_color: get_color_from_hex("#388E3C")
                        on_release: app.show_success("Drafting Request Sent!")

# --- 5. E-CHALLAN SCREEN ---
<ChallanScreen>:
    name: "challan"
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "E-Challan"
            left_action_items: [["arrow-left", lambda x: app.change_screen('main')]]
            md_bg_color: get_color_from_hex("#C2185B")
            elevation: 4
            
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "20dp"
                spacing: "20dp"
                
                MDLabel:
                    text: "Pay Traffic Challan"
                    halign: "center"
                    font_style: "H5"
                    bold: True
                    adaptive_height: True
                
                MDCard:
                    orientation: "vertical"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    padding: "15dp"
                    spacing: "15dp"
                    radius: [15,]
                    adaptive_height: True
                    elevation: 3
                    
                    CommonTextField:
                        hint_text: "Vehicle No. (Ex: DL10AB1234)"
                    
                    CommonTextField:
                        hint_text: "Chassis Last 5 Digits"
                        input_filter: "int"
                        
                    CommonTextField:
                        hint_text: "Mobile Number"
                        input_filter: "int"
                        
                    MDRaisedButton:
                        text: "Check & Pay"
                        size_hint_x: 1
                        md_bg_color: get_color_from_hex("#C2185B")
                        on_release: app.show_success("Checking Challan...")

# --- 6. COUNSEL SCREEN (UPDATED: FORM ONLY) ---
<CounselScreen>:
    name: "counsel"
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "Expert Lawyer Help"
            left_action_items: [["arrow-left", lambda x: app.change_screen('main')]]
            md_bg_color: get_color_from_hex("#7B1FA2")
            elevation: 4
            
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "20dp"
                spacing: "15dp"
                
                MDLabel:
                    text: "Consult a Lawyer"
                    halign: "center"
                    font_style: "H5"
                    bold: True
                    adaptive_height: True
                
                MDLabel:
                    text: "Fill details, we will connect you to the right expert."
                    halign: "center"
                    font_style: "Body2"
                    theme_text_color: "Secondary"
                    adaptive_height: True
                
                MDCard:
                    orientation: "vertical"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    padding: "15dp"
                    spacing: "15dp"
                    radius: [15,]
                    adaptive_height: True
                    elevation: 3
                    
                    CommonTextField:
                        hint_text: "Your Full Name"
                        icon_right: "account"
                    
                    CommonTextField:
                        hint_text: "Mobile Number"
                        icon_right: "phone"
                        input_filter: "int"
                    
                    CommonTextField:
                        hint_text: "Legal Issue (e.g., Divorce, Property)"
                        icon_right: "gavel"
                    
                    # Large Text Box for Details
                    CommonTextField:
                        hint_text: "Describe your case (approx 120 words)..."
                        multiline: True
                        max_height: "150dp"
                        mode: "rectangle"
                    
                    MDRaisedButton:
                        text: "Submit Case Details"
                        size_hint_x: 1
                        md_bg_color: get_color_from_hex("#7B1FA2")
                        on_release: app.show_success("Case details submitted! Our team will call you.")

# --- 7. FEEDBACK SCREEN (NEW) ---
<FeedbackScreen>:
    name: "feedback"
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "Feedback"
            left_action_items: [["arrow-left", lambda x: app.change_screen('main')]]
            md_bg_color: get_color_from_hex("#546E7A")
            elevation: 4
            
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "20dp"
                spacing: "20dp"
                
                MDLabel:
                    text: "We value your feedback"
                    halign: "center"
                    font_style: "H5"
                    bold: True
                    adaptive_height: True
                
                MDCard:
                    orientation: "vertical"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": 0.5}
                    padding: "15dp"
                    spacing: "15dp"
                    radius: [15,]
                    adaptive_height: True
                    elevation: 3
                    
                    CommonTextField:
                        hint_text: "Your Name"
                        
                    CommonTextField:
                        hint_text: "Write your feedback here..."
                        multiline: True
                        max_height: "150dp"
                        
                    MDRaisedButton:
                        text: "Submit Feedback"
                        size_hint_x: 1
                        md_bg_color: get_color_from_hex("#546E7A")
                        on_release: app.show_success("Thank you for your feedback!")
'''

# --- PYTHON CODE ---

class HomeScreenCard(MDCard):
    # Defining StringProperty explicitly to avoid NameError
    icon = StringProperty("")
    text = StringProperty("")
    dest_screen = StringProperty("")

class MainScreen(MDScreen): 
    pass

class GSTScreen(MDScreen): 
    pass

class TaxScreen(MDScreen): 
    pass

class PropertyScreen(MDScreen): 
    pass

class ChallanScreen(MDScreen): 
    pass

class CounselScreen(MDScreen): 
    pass

class FeedbackScreen(MDScreen):
    pass

class LegalHelpDostApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.dialog = None
        return Builder.load_string(KV)
    
    # Removed the on_start lawyer list generation logic 
    # because CounselScreen is now a static form.
    
    def change_screen(self, screen_name):
        self.root.current = screen_name
        
    def show_success(self, text):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Status",
                text=text,
                buttons=[MDRaisedButton(text="OK", on_release=lambda x: self.dialog.dismiss())]
            )
        self.dialog.text = text
        self.dialog.open()
        
    def show_menu(self):
        self.show_success("App Version 1.0\nLegalHelpDost")

if __name__ == '__main__':
    LegalHelpDostApp().run()
