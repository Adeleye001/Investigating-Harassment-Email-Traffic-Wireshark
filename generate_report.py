from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def build_pdf():
    pdf_filename = "Investigating_Harassment_Email_Traffic_Executive_Report.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=54, leftMargin=54,
        topMargin=54, bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#1A365D")  # Deep Navy
    secondary_color = colors.HexColor("#2B6CB0") # Slate Blue
    dark_neutral = colors.HexColor("#2D3748")    # Charcoal
    light_bg = colors.HexColor("#F7FAFC")        # Soft Grey
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=14,
        textColor=secondary_color,
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'Heading1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=dark_neutral,
        spaceAfter=8
    )
    
    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=body_style,
        leftIndent=15,
        spaceAfter=4
    )

    story = []
    
    story.append(Paragraph("Executive Incident Investigation Report", title_style))
    story.append(Paragraph("Case: Analysis of Harassment Traffic via Wireshark / TShark | Ref: SBT-DF203", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceAfter=12))
    
    story.append(Paragraph("1. Case Overview", h1_style))
    story.append(Paragraph(
        "This digital forensics investigation analyzes network packet captures (<b>nitroba.pcap</b>) concerning harassing electronic communications directed at faculty members within the Nitroba University environment. Utilizing TShark analytical tooling, the investigation successfully isolated network endpoints, extracted plaintext payloads, identified hardware MAC addresses, and correlated client session identifiers.",
        body_style
    ))
    
    story.append(Paragraph("2. Forensic Artifact Summary", h1_style))
    
    table_data = [
        [Paragraph("<b>Artifact Category</b>", body_style), Paragraph("<b>Identified Value / Indicator</b>", body_style)],
        [Paragraph("Suspect Local IP", body_style), Paragraph("<code>192.168.15.4</code>", body_style)],
        [Paragraph("Target Web Server IP", body_style), Paragraph("<code>69.25.94.22</code> (<code>www.willselfdestruct.com</code>)", body_style)],
        [Paragraph("Target Recipient", body_style), Paragraph("<code>lilytuckrige@yahoo.com</code> (Faculty Target)", body_style)],
        [Paragraph("Harassment Payload", body_style), Paragraph("\"you can't find us, and you can't hide from us. Stop teaching. Start running.\"", body_style)],
        [Paragraph("Hardware MAC Address", body_style), Paragraph("<code>00:17:f2:e2:c0:ce</code> (Apple NIC)", body_style)],
        [Paragraph("OS & Browser Footprint", body_style), Paragraph("Mac OS X 10.5.4 / Safari 3.1.2", body_style)],
    ]
    
    t = Table(table_data, colWidths=[150, 354])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), light_bg),
        ('TEXTCOLOR', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
    ]))
    
    story.append(t)
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("3. Technical Methodology & Evidence Path", h1_style))
    story.append(Paragraph("The investigation followed rigorous chain-of-custody and analytical standards across structured phases:", body_style))
    story.append(Paragraph("• <b>Phase I (Network Identification):</b> Filtered HTTP traffic to isolate communication between internal subnet IP <code>192.168.15.4</code> and external destinations.", bullet_style))
    story.append(Paragraph("• <b>Phase II (Payload Verification):</b> Parsed URL-encoded form parameters within packet frame <code>83601</code> to confirm exact harassment text.", bullet_style))
    story.append(Paragraph("• <b>Phase III (Hardware Attribution):</b> Extracted Layer 2 Ethernet headers to identify physical manufacturer characteristics.", bullet_style))
    story.append(Paragraph("• <b>Phase IV & V (Session & Client Profiling):</b> Extracted HTTP cookies and User-Agent strings confirming client software footprint.", bullet_style))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("4. Conclusion & Recommendations", h1_style))
    story.append(Paragraph(
        "Corroboration between Layer 2 hardware identifiers (Apple network interface) and Layer 7 client signatures (Mac OS X Safari User-Agent) confirms the suspect device fingerprint. It is recommended to cross-reference physical access logs with the isolated MAC address <code>00:17:f2:e2:c0:ce</code> during the time window of frame <code>83601</code>.",
        body_style
    ))

    doc.build(story)
    print("PDF generated successfully!")

if __name__ == '__main__':
    build_pdf()
