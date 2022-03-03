
A = ["1.1.1", "1.2.1", "1.2.2", "1.2.3", "1.3.1", "1.3.2", "1.3.3", "1.4.1", "1.4.2", "2.1.1", "2.1.2", "2.1.4", "2.2.1", "2.2.2", "2.3.1", "2.4.1", "2.4.2", "2.4.3", "2.4.4", "2.5.1", "2.5.2", "2.5.3", "2.5.4", "3.1.1", "3.2.1", "3.2.2", "3.2.6", "3.3.1", "3.3.2", "3.3.7", "3.3.8", "4.1.1", "4.1.2"]

AA = ["1.2.4", "1.2.5", "1.3.4", "1.3.5", "1.4.3", "1.4.4", "1.4.5", "1.4.10", "1.4.11", "1.4.12", "1.4.13", "2.4.5", "2.4.6", "2.4.7", "2.5.7", "2.5.8", "3.1.2", "3.2.3", "3.2.4", "3.2.7", "3.3.3", "3.3.4", "4.1.3"]

AAA = ["1.2.6", "1.2.7", "1.2.8", "1.2.9", "1.3.6", "1.4.6", "1.4.7", "1.4.8", "1.4.9", "2.1.3", "2.2.3", "2.2.4", "2.2.5", "2.2.6", "2.3.2", "2.3.3", "2.4.8", "2.4.9", "2.4.10", "2.5.5", "2.5.6", "3.1.3", "3.1.4", "3.1.5", "3.1.6", "3.2.5", "3.3.5", "3.3.6"]

macroareas = {
"1.1.":"Text Alternatives",
"1.2.":"Time-based Media",
"1.3.":"Adaptable",
"1.4.":"Distinguishable",
"2.1.":"Keyboard Accessible",
"2.2.":"Enough Time",
"2.3.":"Seizures and Physical Reactions",
"2.4.":"Navigable",
"2.5.":"Input Modalities",
"3.1.":"Readable",
"3.2.":"Predictable",
"3.3.":"Input Assistance",
"4.1.":"Compatible",
"5.1.":"Interpreting Normative Requirements",
"5.2.":"Conformance Requirements",
"5.3.":"Conformance Claims (Optional)",
"5.4.":"Statement of Partial Conformance - Third Party Content",
"5.5.":"Statement of Partial Conformance - Language"
}

guidelines = {
"1.1.1":["Non-text Content","https://www.w3.org/TR/WCAG22/#non-text-content"],
"1.2.1":["Audio-only and Video-only (Prerecorded)","https://www.w3.org/TR/WCAG22/#audio-only-and-video-only-prerecorded"],
"1.2.2":["Captions (Prerecorded)","https://www.w3.org/TR/WCAG22/#captions-prerecorded"],
"1.2.3":["Audio Description or Media Alternative (Prerecorded)","https://www.w3.org/TR/WCAG22/#audio-description-or-media-alternative-prerecorded"],
"1.2.4":["Captions (Live)","https://www.w3.org/TR/WCAG22/#captions-live"],
"1.2.5":["Audio Description (Prerecorded)","https://www.w3.org/TR/WCAG22/#audio-description-prerecorded"],
"1.2.6":["Sign Language (Prerecorded)","https://www.w3.org/TR/WCAG22/#sign-language-prerecorded"],
"1.2.7":["Extended Audio Description (Prerecorded)","https://www.w3.org/TR/WCAG22/#extended-audio-description-prerecorded"],
"1.2.8":["Media Alternative (Prerecorded)","https://www.w3.org/TR/WCAG22/#media-alternative-prerecorded"],
"1.2.9":["Audio-only (Live)","https://www.w3.org/TR/WCAG22/#audio-only-live"],
"1.3.1":["Info and Relationships","https://www.w3.org/TR/WCAG22/#info-and-relationships"],
"1.3.2":["Meaningful Sequence","https://www.w3.org/TR/WCAG22/#meaningful-sequence"],
"1.3.3":["Sensory Characteristics","https://www.w3.org/TR/WCAG22/#sensory-characteristics"],
"1.3.4":["Orientation","https://www.w3.org/TR/WCAG22/#orientation"],
"1.3.5":["Identify Input Purpose","https://www.w3.org/TR/WCAG22/#identify-input-purpose"],
"1.3.6":["Identify Purpose","https://www.w3.org/TR/WCAG22/#identify-purpose"],
"1.4.1":["Use of Color","https://www.w3.org/TR/WCAG22/#use-of-color"],
"1.4.2":["Audio Control","https://www.w3.org/TR/WCAG22/#audio-control"],
"1.4.3":["Contrast (Minimum)","https://www.w3.org/TR/WCAG22/#contrast-minimum"],
"1.4.4":["Resize text","https://www.w3.org/TR/WCAG22/#resize-text"],
"1.4.5":["Images of Text","https://www.w3.org/TR/WCAG22/#images-of-text"],
"1.4.6":["Contrast (Enhanced)","https://www.w3.org/TR/WCAG22/#contrast-enhanced"],
"1.4.7":["Low or No Background Audio","https://www.w3.org/TR/WCAG22/#low-or-no-background-audio"],
"1.4.8":["Visual Presentation","https://www.w3.org/TR/WCAG22/#visual-presentation"],
"1.4.9":["Images of Text (No Exception)","https://www.w3.org/TR/WCAG22/#images-of-text-no-exception"],
"1.4.10":["Reflow","https://www.w3.org/TR/WCAG22/#reflow"],
"1.4.11":["Non-text Contrast","https://www.w3.org/TR/WCAG22/#non-text-contrast"],
"1.4.12":["Text Spacing","https://www.w3.org/TR/WCAG22/#text-spacing"],
"1.4.13":["Content on Hover or Focus","https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus"],
"2.1.1":["Keyboard","https://www.w3.org/TR/WCAG22/#keyboard"],
"2.1.2":["No Keyboard Trap","https://www.w3.org/TR/WCAG22/#no-keyboard-trap"],
"2.1.3":["Keyboard (No Exception)","https://www.w3.org/TR/WCAG22/#keyboard-no-exception"],
"2.1.4":["Character Key Shortcuts","https://www.w3.org/TR/WCAG22/#character-key-shortcuts"],
"2.2.1":["Timing Adjustable","https://www.w3.org/TR/WCAG22/#timing-adjustable"],
"2.2.2":["Pause, Stop, Hide","https://www.w3.org/TR/WCAG22/#pause-stop-hide"],
"2.2.3":["No Timing","https://www.w3.org/TR/WCAG22/#no-timing"],
"2.2.4":["Interruptions","https://www.w3.org/TR/WCAG22/#interruptions"],
"2.2.5":["Re-authenticating","https://www.w3.org/TR/WCAG22/#re-authenticating"],
"2.2.6":["Timeouts","https://www.w3.org/TR/WCAG22/#timeouts"],
"2.3.1":["Three Flashes or Below Threshold","https://www.w3.org/TR/WCAG22/#three-flashes-or-below-threshold"],
"2.3.2":["Three Flashes","https://www.w3.org/TR/WCAG22/#three-flashes"],
"2.3.3":["Animation from Interactions","https://www.w3.org/TR/WCAG22/#animation-from-interactions"],
"2.4.1":["Bypass Blocks","https://www.w3.org/TR/WCAG22/#bypass-blocks"],
"2.4.2":["Page Titled","https://www.w3.org/TR/WCAG22/#page-titled"],
"2.4.3":["Focus Order","https://www.w3.org/TR/WCAG22/#focus-order"],
"2.4.4":["Link Purpose (In Context)","https://www.w3.org/TR/WCAG22/#link-purpose-in-context"],
"2.4.5":["Multiple Ways","https://www.w3.org/TR/WCAG22/#multiple-ways"],
"2.4.6":["Headings and Labels","https://www.w3.org/TR/WCAG22/#headings-and-labels"],
"2.4.7":["Focus Visible","https://www.w3.org/TR/WCAG22/#focus-visible"],
"2.4.8":["Location","https://www.w3.org/TR/WCAG22/#location"],
"2.4.9":["Link Purpose (Link Only)","https://www.w3.org/TR/WCAG22/#link-purpose-link-only"],
"2.4.10":["Section Headings","https://www.w3.org/TR/WCAG22/#section-headings"],
"2.4.11":["Focus Appearance (Minimum)","https://www.w3.org/TR/WCAG22/#focus-appearance-minimum"],
"2.4.12":["Focus Appearance (Enhanced)","https://www.w3.org/TR/WCAG22/#focus-appearance-enhanced"],
"2.4.13":["Page Break Navigation","https://www.w3.org/TR/WCAG22/#page-break-navigation"],
"2.5.1":["Pointer Gestures","https://www.w3.org/TR/WCAG22/#pointer-gestures"],
"2.5.2":["Pointer Cancellation","https://www.w3.org/TR/WCAG22/#pointer-cancellation"],
"2.5.3":["Label in Name","https://www.w3.org/TR/WCAG22/#label-in-name"],
"2.5.4":["Motion Actuation","https://www.w3.org/TR/WCAG22/#motion-actuation"],
"2.5.5":["Target Size (Enhanced)","https://www.w3.org/TR/WCAG22/#target-size-enhanced"],
"2.5.6":["Concurrent Input Mechanisms","https://www.w3.org/TR/WCAG22/#concurrent-input-mechanisms"],
"2.5.7":["Dragging Movements","https://www.w3.org/TR/WCAG22/#dragging-movements"],
"2.5.8":["Target Size (Minimum)","https://www.w3.org/TR/WCAG22/#target-size-minimum"],
"3.1.1":["Language of Page","https://www.w3.org/TR/WCAG22/#language-of-page"],
"3.1.2":["Language of Parts","https://www.w3.org/TR/WCAG22/#language-of-parts"],
"3.1.3":["Unusual Words","https://www.w3.org/TR/WCAG22/#unusual-words"],
"3.1.4":["Abbreviations","https://www.w3.org/TR/WCAG22/#abbreviations"],
"3.1.5":["Reading Level","https://www.w3.org/TR/WCAG22/#reading-level"],
"3.1.6":["Pronunciation","https://www.w3.org/TR/WCAG22/#pronunciation"],
"3.2.1":["On Focus","https://www.w3.org/TR/WCAG22/#on-focus"],
"3.2.2":["On Input","https://www.w3.org/TR/WCAG22/#on-input"],
"3.2.3":["Consistent Navigation","https://www.w3.org/TR/WCAG22/#consistent-navigation"],
"3.2.4":["Consistent Identification","https://www.w3.org/TR/WCAG22/#consistent-identification"],
"3.2.5":["Change on Request","https://www.w3.org/TR/WCAG22/#change-on-request"],
"3.2.6":["Consistent Help","https://www.w3.org/TR/WCAG22/#consistent-help"],
"3.2.7":["Visible Controls","https://www.w3.org/TR/WCAG22/#visible-controls"],
"3.3.1":["Error Identification","https://www.w3.org/TR/WCAG22/#error-identification"],
"3.3.2":["Labels or Instructions","https://www.w3.org/TR/WCAG22/#labels-or-instructions"],
"3.3.3":["Error Suggestion","https://www.w3.org/TR/WCAG22/#error-suggestion"],
"3.3.4":["Error Prevention (Legal, Financial, Data)","https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data"],
"3.3.5":["Help","https://www.w3.org/TR/WCAG22/#help"],
"3.3.6":["Error Prevention (All)","https://www.w3.org/TR/WCAG22/#error-prevention-all"],
"3.3.7":["Accessible Authentication","https://www.w3.org/TR/WCAG22/#accessible-authentication"],
"3.3.8":["Redundant entry","https://www.w3.org/TR/WCAG22/#redundant-entry"],
"4.1.1":["Parsing","https://www.w3.org/TR/WCAG22/#parsing"],
"4.1.2":["Name, Role, Value","https://www.w3.org/TR/WCAG22/#name-role-value"],
"4.1.3":["Status Messages","https://www.w3.org/TR/WCAG22/#status-messages"]
}

WCAG2_2 = ["2.4.11", "2.4.12", "2.4.13", "2.5.7", "2.5.8", "3.2.6", "3.2.7", "3.3.7", "3.3.8"]