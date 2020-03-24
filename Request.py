<!DOCTYPE html>
<!-- saved from url=(0040)https://realpython.com/python-interface/ -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><script src="./Request_files/amp4ads-host-v0.js"></script><script src="./Request_files/osd.js"></script><script src="./Request_files/pubads_impl_rendering_2020030501.js"></script><script src="./Request_files/jquery.color-2.1.2.min.js"></script><script type="text/javascript" src="./Request_files/track"></script><script type="text/javascript" async="" src="./Request_files/client.js"></script><script src="./Request_files/2220911568135371" async=""></script><script async="" src="./Request_files/fbevents.js"></script><script type="text/javascript" async="" src="./Request_files/6214500.js"></script><script type="text/javascript" async="" src="./Request_files/videoplayer.js"></script><script type="text/javascript" async="" src="./Request_files/prebid.js"></script>
<link href="https://files.realpython.com/" rel="preconnect">
<title>Implementing an Interface in Python – Real Python</title>
<meta name="author" content="Real Python">
<meta name="description" content="In this tutorial, you&#39;ll explore how to use a Python interface. You&#39;ll come to understand why interfaces are so useful and learn how to implement formal and informal interfaces in Python. You&#39;ll also examine the differences between Python interfaces and those in other programming languages.">
<meta name="keywords" content="">

<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="./Request_files/font.32be62914940.css">
<link rel="stylesheet" href="./Request_files/realpython.min.0e2802036907.css">
<link rel="canonical" href="https://realpython.com/python-interface/">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://files.realpython.com/media/Interfaces-in-Python_Watermarked.f9ce5bda238c.jpg">
<meta property="og:image" content="https://files.realpython.com/media/Interfaces-in-Python_Watermarked.f9ce5bda238c.jpg">
<meta name="twitter:creator" content="@realpython">
<meta name="twitter:site" content="@realpython">
<meta property="og:title" content="Implementing an Interface in Python – Real Python">
<meta property="og:type" content="article">
<meta property="og:url" content="https://realpython.com/python-interface/">
<meta property="og:description" content="In this tutorial, you&#39;ll explore how to use a Python interface. You&#39;ll come to understand why interfaces are so useful and learn how to implement formal and informal interfaces in Python. You&#39;ll also examine the differences between Python interfaces and those in other programming languages.">
<link href="https://realpython.com/static/favicon.68cbf4197b0c.png" rel="icon">
<link href="https://realpython.com/atom.xml" rel="alternate" title="Real Python" type="application/atom+xml">
<link rel="manifest" href="https://realpython.com/manifest.json">
<script async="" type="text/javascript" src="./Request_files/gpt.js"></script><script async="" src="./Request_files/analytics.js"></script><script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-35184939-1', 'auto', {'allowLinker': true});
  
  
  ga('send', 'pageview');
  
</script>
<style type="text/css">#waldo-sticky-footer-wrapper {position: fixed; width: 100%; bottom: 0px; left: 0px; text-align: center; z-index: 9000;}#waldo-sticky-footer-wrapper > div {position: relative; display: inline-block}#waldo-sticky-footer-wrapper iframe, #waldo-sticky-footer-wrapper div {margin-left: auto;margin-right: auto;}.waldo-sticky-sidebar{position: fixed; top: 10px;z-index: 90}.waldo-sticky-css{position: sticky; top: 10px; z-index: 90}.waldo-overlay{position: fixed;height: 100%;width: 100%;top: 0;left: 0;z-index: 105;background: rgba(0,0,0,0.7);}#waldo-counter {position: absolute;bottom: 0;right: 0;color: #fff;font-size: 30px;padding: 15px;}#waldo-tag-6038 {clear: both !important;}div[class^="app_gdpr-"] a {color: #41afbb !important; text-decoration: underline !important}#waldo-close-button {position: absolute; right: 0;top: -24px;}#waldo-close-button a {border: 1px solid rgba(0,0,0,.35);padding: 3px;font-size: 12px;color: #fff;font-weight: bold;background-color: #777;}</style><script type="text/javascript">googletag.cmd.push(function() {googletag.pubads().addEventListener('slotRenderEnded', function(event) {waldoAddCloseBtn(event);});googletag.pubads().enableSingleRequest();googletag.enableServices();gptAdSlots[4996] = googletag.defineSlot('/124067137/realpython728x90FS_1', [[728, 90], [300, 250], [320, 50]], 'waldo-tag-4996').defineSizeMapping(googletag.sizeMapping().addSize([1024, 0], [[728, 90], [300, 250]]).addSize([768, 0], [[300, 250], [320, 50]]).addSize([0, 0], [[300, 250], [320, 50]]).build()).addService(googletag.pubads());googletag.display('waldo-tag-4996');gptAdSlots[4998] = googletag.defineSlot('/124067137/realpython728x90FS_2', [[728, 90], [300, 250], [320, 50]], 'waldo-tag-4998').defineSizeMapping(googletag.sizeMapping().addSize([1024, 0], [[728, 90], [300, 250]]).addSize([768, 0], [[300, 250], [320, 50]]).addSize([0, 0], [[300, 250], [320, 50]]).build()).addService(googletag.pubads());googletag.display('waldo-tag-4998');gptAdSlots[5000] = googletag.defineSlot('/124067137/realpython728x90FS_3', [[728, 90], [300, 250], [320, 50]], 'waldo-tag-5000').defineSizeMapping(googletag.sizeMapping().addSize([1024, 0], [[728, 90], [300, 250]]).addSize([768, 0], [[300, 250], [320, 50]]).addSize([0, 0], [[300, 250], [320, 50]]).build()).addService(googletag.pubads());googletag.display('waldo-tag-5000');gptAdSlots[5002] = googletag.defineSlot('/124067137/realpython728x90FS_4', [[728, 90], [300, 250], [320, 50]], 'waldo-tag-5002').defineSizeMapping(googletag.sizeMapping().addSize([1024, 0], [[728, 90], [300, 250]]).addSize([768, 0], [[300, 250], [320, 50]]).addSize([0, 0], [[300, 250], [320, 50]]).build()).addService(googletag.pubads());googletag.display('waldo-tag-5002');gptAdSlots[5004] = googletag.defineSlot('/124067137/realpython728x90FS_5', [[728, 90], [300, 250], [320, 50]], 'waldo-tag-5004').defineSizeMapping(googletag.sizeMapping().addSize([1024, 0], [[728, 90], [300, 250]]).addSize([768, 0], [[300, 250], [320, 50]]).addSize([0, 0], [[300, 250], [320, 50]]).build()).addService(googletag.pubads());googletag.display('waldo-tag-5004');});</script><script src="./Request_files/count-data.js"></script><script src="./Request_files/OneSignalPageSDKES6.js" async=""></script><link rel="preload" href="./Request_files/f(4).txt" as="script"><script type="text/javascript" src="./Request_files/f(4).txt"></script><script src="./Request_files/pubads_impl_2020030501.js" async=""></script><link rel="stylesheet" href="./Request_files/OneSignalSDKStyles.css"><style type="text/css">
  /* === Form-Specific Styles === */
  /* stylelint-disable */

  #drip-106703 {
  }

  #drip-106703 .drip-header {
    background-color: #43ac6a !important;
  }

  #drip-106703 .drip-content h3 {
    color: #43ac6a !important;
    font-size: 29px !important;
  }

  #drip-106703 .drip-submit-button {
    background-color: #43ac6a !important;
    font-size: 19px !important;
  }

  #drip-106703 .drip-submit-button:hover {
    background-color: #40a365 !important;
  }

  #drip-106703 .drip-submit-button:active {
    background-color: #3c9b5f !important;
  }

  #drip-106703 dl dt,
  #drip-106703 .drip-content .drip-description,
  #drip-106703 .drip-errors {
    font-size: 18px !important;
  }

  #drip-106703 .drip-text-field {
    font-size: 18px !important;
  }

  /* === Reset styles === */

  .drip-tab h1,
  .drip-tab h2,
  .drip-tab h3,
  .drip-tab div,
  .drip-tab dl,
  .drip-tab dt,
  .drip-tab dd,
  .drip-tab p,
  .drip-tab a,
  .drip-tab .drip-text-field,
  .drip-tab .drip-text-field:focus,
  .drip-tab .drip-submit-button {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
    float: none;
    width: auto;
    background-image: none;
    letter-spacing: 0;
    -webkit-box-shadow: none;
       -moz-box-shadow: none;
            box-shadow: none;
    -webkit-text-shadow: none !important;
       -moz-text-shadow: none !important;
            text-shadow: none !important;
  }

  .drip-tab a {
    text-decoration: none;
    color: #43ac6a !important;
  }

  .drip-tab :focus {
    outline: 0;
  }

  /* === Clearfix === */

  .drip-clearfix:after {
    visibility: hidden;
    display: block;
    font-size: 0;
    content: " ";
    clear: both;
    height: 0;
  }
  * html .drip-clearfix             { zoom: 1; } /* IE6 */
  *:first-child+html .drip-clearfix { zoom: 1; } /* IE7 */

  /* === Main Container === */

  .drip-tab-container * {
    box-sizing: content-box;
  }

  /* === Content === */

  .drip-tab .drip-content {
    margin: 0;
    padding: 0;
    width: 380px;
    position: fixed;
    font-size: 100%;
    font: inherit;
    z-index: 10000;
    color: #333;
    vertical-align: baseline;
    text-align: left;
    background-color: #ffffff;
    -webkit-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
       -moz-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
            box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
  }

  .drip-tab.bottom .drip-content {
    bottom: -800px;
    -webkit-border-radius: 8px 8px 0 0;
       -moz-border-radius: 8px 8px 0 0;
            border-radius: 8px 8px 0 0;
    -webkit-transition: bottom 200ms ease-in;
       -moz-transition: bottom 200ms ease-in;
         -o-transition: bottom 200ms ease-in;
            transition: bottom 200ms ease-in;
  }

  .drip-tab.bottom.left .drip-content {
    left: 40px;
  }

  .drip-tab.bottom.right .drip-content {
    right: 40px;
  }

  .drip-tab.side-image .drip-content {
    width: 650px;
  }

  .drip-tab.side .drip-content {
    top: 10%;
  }

  .drip-tab.side.right .drip-content {
    right: -675px;
    -webkit-border-radius: 8px 0 0 8px;
       -moz-border-radius: 8px 0 0 8px;
            border-radius: 8px 0 0 8px;
    -webkit-transition: right 200ms ease-in;
       -moz-transition: right 200ms ease-in;
         -o-transition: right 200ms ease-in;
            transition: right 200ms ease-in;
  }

  .drip-tab.side.left .drip-content {
    left: -675px;
    -webkit-border-radius: 0 8px 8px 0;
       -moz-border-radius: 0 8px 8px 0;
            border-radius: 0 8px 8px 0;
    -webkit-transition: left 200ms ease-in;
       -moz-transition: left 200ms ease-in;
         -o-transition: left 200ms ease-in;
            transition: left 200ms ease-in;
  }

  .drip-tab.mobile .drip-content {
    width: 100% !important;
    bottom: -800px;
    left: 0;
    -webkit-border-radius: 0;
       -moz-border-radius: 0;
            border-radius: 0;
    -webkit-transition: bottom 200ms ease-in;
       -moz-transition: bottom 200ms ease-in;
         -o-transition: bottom 200ms ease-in;
            transition: bottom 200ms ease-in;
  }

  .drip-tab.drip-scrollable .drip-content {
    overflow-y: scroll;
  }

  /* === Header === */

  .drip-tab .drip-header {
    margin: 0;
    padding: 0;
    position: fixed;
    font-size: 100%;
    font: inherit;
    z-index: 10000;
    color: #333;
    vertical-align: baseline;
    text-align: left;
    -webkit-border-radius: 8px 8px 0 0;
       -moz-border-radius: 8px 8px 0 0;
            border-radius: 8px 8px 0 0;
    -webkit-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
       -moz-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
            box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
  }

  .drip-tab.bottom .drip-header {
    width: 380px;
    bottom: 0;
    -webkit-transition: bottom 200ms ease-in;
       -moz-transition: bottom 200ms ease-in;
         -o-transition: bottom 200ms ease-in;
            transition: bottom 200ms ease-in;
  }

  .drip-tab.bottom .drip-header.drip-hidden {
    bottom: -800px;
  }

  .drip-tab.bottom.left .drip-header {
    left: 40px;
  }

  .drip-tab.bottom.right .drip-header {
    right: 40px;
  }

  .drip-tab.bottom.image-left .drip-header,
  .drip-tab.bottom.image-right .drip-header {
    width: 510px;
  }

  .drip-tab.side .drip-header {
    width: 340px;
    top: 10%;
  }

  .drip-tab.side.right .drip-header {
    right: -100px;
    -webkit-transition: right 400ms ease-in;
       -moz-transition: right 400ms ease-in;
         -o-transition: right 400ms ease-in;
            transition: right 400ms ease-in;
    -webkit-transform: rotate(-90deg) !important;
       -moz-transform: rotate(-90deg) !important;
        -ms-transform: rotate(-90deg) !important;
         -o-transform: rotate(-90deg) !important;
            transform: rotate(-90deg) !important;
    -webkit-transform-origin: right center;
       -moz-transform-origin: right center;
         -o-transform-origin: right center;
            transform-origin: right center;
  }

  .drip-tab.side.right .drip-header.drip-hidden {
    right: -100px;
  }

  .drip-tab.side.left .drip-header {
    left: -100px;
    -webkit-transition: left 400ms ease-in;
       -moz-transition: left 400ms ease-in;
         -o-transition: left 400ms ease-in;
            transition: left 400ms ease-in;
    -webkit-transform: rotate(90deg) !important;
       -moz-transform: rotate(90deg) !important;
        -ms-transform: rotate(90deg) !important;
         -o-transform: rotate(90deg) !important;
            transform: rotate(90deg) !important;
    -webkit-transform-origin: left center;
       -moz-transform-origin: left center;
         -o-transform-origin: left center;
            transform-origin: left center;
  }

  .drip-tab.side.left .drip-header.drip-hidden {
    left: -100px;
  }

  .drip-tab.mobile .drip-header {
    width: 100% !important;
    bottom: 0;
    left: 0;
    -webkit-border-radius: 0;
       -moz-border-radius: 0;
            border-radius: 0;
    -webkit-transition: bottom 200ms ease-in;
       -moz-transition: bottom 200ms ease-in;
         -o-transition: bottom 200ms ease-in;
            transition: bottom 200ms ease-in;
  }

  .drip-tab.mobile .drip-header.drip-hidden {
    bottom: -300px;
  }

  /* === Header Toggle === */

  .drip-tab .drip-toggle {
    display: block;
    text-decoration: none;
    padding: 10px 50px 10px 25px; /* extra padding for the arrow */
  }

  /* === Teaser === */

  .drip-tab .drip-header h2 {
    display: block;
    margin: 0 !important;
    padding: 0 !important;
    border: 0 !important;
    font-size: 16px !important;
    line-height: 1.5 !important;
    font-weight: bold !important;
    text-align: left !important;
    color: #fff !important;
    clear: none !important;
    letter-spacing: 0 !important;
    width: auto !important;
  }

  /* === Arrows === */

  .drip-tab .drip-header span.drip-arrow {
    display: block;
    position: absolute;
    margin: 0;
    padding: 0;
    width: 0;
    height: 0;
    line-height: 0;
    top: 20px;
    right: 32px;
  }

  /* === Panel === */

  .drip-tab .drip-content > div.drip-panel {
    padding: 25px;
    background-color: #fff;
    -webkit-border-radius: 6px;
       -moz-border-radius: 6px;
            border-radius: 6px;
  }

  .drip-tab.bottom .drip-content > div.drip-panel {
    -webkit-border-radius: 6px 6px 0 0;
       -moz-border-radius: 6px 6px 0 0;
            border-radius: 6px 6px 0 0;
  }

  .drip-tab.side.left .drip-content > div.drip-panel {
    -webkit-border-radius: 0 6px 6px 0;
       -moz-border-radius: 0 6px 6px 0;
            border-radius: 0 6px 6px 0;
  }

  .drip-tab.side.right .drip-content > div.drip-panel  {
    -webkit-border-radius: 6px 0 0 6px;
       -moz-border-radius: 6px 0 0 6px;
            border-radius: 6px 0 0 6px;
  }

  /* === Powered By === */

  .drip-tab .drip-powered-by {
    padding: 8px;
    text-align: left;
    font-weight: normal;
    font-size: 10px;
    line-height: 16px;
    color: #A8ACB9;
    text-align: right;
    margin-right: 25px;
    text-transform: uppercase;
    display: -webkit-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }

  .drip-tab .drip-powered-by a {
    color: #A8ACB9 !important;
    text-decoration: underline !important;
    margin-left: 6px;
  }

  /* === Content Sections === */

  .drip-tab.side-image .drip-form-aside {
    width: 245px;
    text-align: center;
  }

  .drip-tab.image-left .drip-form-main {
    margin-left: 270px;
  }

  .drip-tab.image-right .drip-form-main {
    margin-right: 270px;
  }

  .drip-tab.image-left .drip-form-aside {
    float: left;
  }

  .drip-tab.image-right .drip-form-aside {
    float: right;
  }

  @media screen and (max-width: 650px) {
    .drip-tab.side-image .drip-content {
      width: 380px;
    }

    .drip-tab.side-image .drip-form-main {
      margin-left: 0;
      margin-right: 0;
    }

    .drip-tab.side-image .drip-form-aside {
      display: none;
    }
  }

  /* === Content Headings & Paragraphs === */

  .drip-tab .drip-content h3 {
    display: block;
    margin: 0 20px 0 0 !important;
    padding: 0 0 15px 0 !important;
    line-height: 1.4 !important;
    font-weight: bold !important;
    text-align: left !important;
    color: #4477bd !important;
    clear: none !important;
  }

  .drip-tab .drip-content .drip-description {
    margin: 0;
    padding: 0 0 20px 0;
    line-height: 1.4;
    text-align: left;
    color: #4F5362;
  }

  .drip-tab .drip-content .drip-post-submission {
    padding: 0;
  }

  .drip-tab .drip-content .drip-description a {
    text-decoration: underline;
  }

  .drip-tab .drip-content .drip-description em {
    font-style: italic;
  }

  .drip-tab .drip-content .drip-description ul,
  .drip-tab .drip-content .drip-description ol {
    list-style-position: outside;
    margin: 8px 0 8px 30px;
  }

  .drip-tab .drip-content .drip-description ul li
  .drip-tab .drip-content .drip-description ol li {
    padding: 0;
  }

  .drip-tab .drip-content .drip-image-center-helper {
    display: inline-block;
    height: 100%;
    vertical-align: middle;
  }

  .drip-tab .drip-content img.drip-image {
    max-width: 245px;
    vertical-align: middle;
  }

  .drip-tab .drip-content a.drip-close {
    position: absolute;
    right: 25px;
    top: 25px;
  }

  .drip-tab .drip-content a.drip-close:hover {
    cursor: pointer;
  }

  /* === Content Subscribe Form === */

  .drip-tab form {
    margin: 0 !important;
    padding: 0 !important;
  }

  .drip-tab dl {
    display: block;
    margin: 0;
    padding: 0 0 5px 0;
  }

  .drip-tab dl dt {
    display: block;
    padding: 0 0 5px 0;
    font-weight: bold;
    color: #4F5362;
  }

  .drip-tab dl.no-labels dt {
    display: none;
  }

  .drip-tab dl dd {
    display: block;
    padding: 0 0 8px 0;
  }

  .drip-tab .drip-text-field {
    margin: 0 !important;
    padding: 10px 12px !important;
    height: auto !important;
    width: 100% !important;
    color: #4F5362 !important;
    background-color: #fff !important;
    border: 1px solid #A8ACB9 !important;
    -webkit-border-radius: 3px !important;
       -moz-border-radius: 3px !important;
            border-radius: 3px !important;
    -webkit-box-sizing: border-box !important;
       -moz-box-sizing: border-box !important;
        -ms-box-sizing: border-box !important;
            box-sizing: border-box !important;
    background-image: none !important;
    min-width: 0 !important;
    min-height: 0 !important;
  }

  .drip-tab .drip-text-field::-webkit-input-placeholder { /* WebKit browsers */
    color: #A8ACB9 !important;
  }
  .drip-tab .drip-text-field:-moz-placeholder { /* Mozilla Firefox 4 to 18 */
    color: #A8ACB9 !important;
  }
  .drip-tab .drip-text-field::-moz-placeholder { /* Mozilla Firefox 19+ */
    color: #A8ACB9 !important;
  }
  .drip-tab .drip-text-field:-ms-input-placeholder { /* Internet Explorer 10+ */
    color: #A8ACB9 !important;
  }

  .drip-tab .drip-text-field:focus {
    border-color: #9398a9 !important;
    outline: 0;
    background-image: none;
    background-color: #fff !important;
  }

  .drip-tab.mobile .drip-text-field {
    font-size: 16px;
  }

  .drip-tab .drip-errors {
    padding: 5px 0 0 0;
    font-weight: normal;
    color: red;
  }

  .drip-tab .drip-submit-button {
    padding: 6px 26px !important;
    color: #ffffff !important;
    font-weight: bold !important;
    line-height: 1.6 !important;
    border: 0 !important;
    -webkit-border-radius: 3px !important;
       -moz-border-radius: 3px !important;
            border-radius: 3px !important;
    cursor: pointer !important;
    background-image: none !important;
    min-width: 0 !important;
    min-height: 0 !important;
    height: auto;
    transition: background 0.2s ease !important;
  }

  .drip-tab .drip-submit-button:hover {
    background-image: none !important;
  }

  .drip-tab .drip-submit-button:active {
    background-image: none !important;
  }

  /* checkbox */

  .drip-tab input,
  .drip-tab textarea {
    display: block;
    box-shadow: none;
    position: relative;
    border: 1px solid #cccccc;
    outline: none;
    border-radius: 3px;
    font: inherit;
    color: #262626;
    padding: 12px 18px;
    transition: border-color 300ms;
    width: 100%;
  }

  .drip-tab .zenput--checkbox.hidden {
    margin-bottom: -8px;
    display: none;
  }

  .drip-tab .zenput--checkbox input[type="checkbox"] {
    height: 0;
    width: 0;
    opacity: 0;
    position: absolute;
    top: 0;
    left: 0;
  }

  .drip-tab .zenput--checkbox input[type="checkbox"] ~ .zenput__checkbox-label {
    font: inherit;
    font-size: 16px;
    line-height: 30px;
    color: #262626;
    cursor: pointer;
    white-space: normal;
    word-break: normal;
    display: block;
    padding-left: 36px;
    position: relative;
    transition: color 300ms
  }

  .drip-tab .zenput--checkbox input[type="checkbox"]~ .zenput__checkbox-label .zenput__checkbox-label__icon {
    content: "";
    display: block;
    background: #f5f5f5;
    width: 24px;
    height: 24px;
    position: absolute;
    top: 3px;
    left: 0;
    border-radius: 3px;
    border: 1px solid #cccccc;
    box-sizing: border-box;
    padding: 3px;
    transition: background 300ms ease-out, border-color 300ms;
  }

  .drip-tab .zenput--checkbox input[type="checkbox"] ~ .zenput__checkbox-label .zenput__checkbox-label__icon svg {
    opacity: 0;
    width: 16px;
    display: block;
    fill: #cccccc;
    transition: opacity 300ms ease-out;
  }

  .drip-tab .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label {
    color: #333 !important;
  }
  .drip-tab .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label .zenput__checkbox-label__icon {
    background-color: #ffffff;
    border-color: #a8acb9;
  }
  .drip-tab .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label .zenput__checkbox-label__icon svg {
    fill: #43ac6a !important;
    opacity: 1;
  }

  /* hover state */

  .drip-tab .zenput--checkbox input:not([disabled]):not(:checked) ~ .zenput__checkbox-label:hover {
    color: #262626;
  }

  .drip-tab .zenput--checkbox input:not([disabled]):not(:checked) ~ .zenput__checkbox-label:hover  .zenput__checkbox-label__icon {
    border-color: var(--gray-9);
  }

  .drip-tab .zenput--checkbox input:not([disabled]):not(:checked) ~ .zenput__checkbox-label:hover  .zenput__checkbox-label__icon svg {
    opacity: 1;
  }

  /* active state */

  .drip-tab .zenput--checkbox input:not([disabled]) ~ .zenput__checkbox-label:active {
    color: #f224f2;
  }

  /* focus state */

  .drip-tab .zenput--checkbox input:not([disabled]) ~ .zenput__checkbox-label:focus .zenput__checkbox-label__icon,
  .drip-tab .zenput--checkbox input:not([disabled]):focus ~ .zenput__checkbox-label .zenput__checkbox-label__icon {
    border-color: #262626;
  }

  /* stylelint-enable */

</style><style type="text/css">
  /* === Form-Specific Styles === */
  /* stylelint-disable */

  #drip-108609 {
    background: #fff !important;
  }

  #drip-108609 .drip-content h3 {
    color: #f9a82f !important;
    font-size: 28px !important;
  }

  #drip-108609 .drip-submit-button {
    background-color: #f9a82f !important;
    font-size: 19px !important;
  }

  #drip-108609 .drip-submit-button:hover {
    background-color: #eda02d !important;
  }

  #drip-108609 .drip-submit-button:active {
    background-color: #e0972a !important;
  }

  #drip-108609 dl dt,
  #drip-108609 .drip-content .drip-description,
  #drip-108609 .drip-errors {
    font-size: 16px !important;
  }

  #drip-108609 .drip-text-field {
    font-size: 16px !important;
  }

  /* === Reset styles === */

  .drip-lightbox h1,
  .drip-lightbox h2,
  .drip-lightbox h3,
  .drip-lightbox div,
  .drip-lightbox dl,
  .drip-lightbox dt,
  .drip-lightbox dd,
  .drip-lightbox p,
  .drip-lightbox a,
  .drip-lightbox .drip-text-field,
  .drip-lightbox .drip-text-field:focus,
  .drip-lightbox .drip-submit-button {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
    float: none;
    width: auto;
    background-image: none;
    letter-spacing: 0;
    -webkit-box-shadow: none;
       -moz-box-shadow: none;
            box-shadow: none;
    -webkit-text-shadow: none !important;
       -moz-text-shadow: none !important;
            text-shadow: none !important;
  }

  .drip-lightbox a {
    text-decoration: none;
    color: #f9a82f !important;
  }

  .drip-lightbox :focus {
    outline: 0;
  }

  .drip-lightbox input::-webkit-input-placeholder { /* WebKit browsers */
    color: #A8ACB9 !important;
  }
  .drip-lightbox input:-moz-placeholder { /* Mozilla Firefox 4 to 18 */
    color: #A8ACB9 !important;
  }
  .drip-lightbox input::-moz-placeholder { /* Mozilla Firefox 19+ */
    color: #A8ACB9 !important;
  }
  .drip-lightbox input:-ms-input-placeholder { /* Internet Explorer 10+ */
    color: #A8ACB9 !important;
  }

  /* === Clearfix === */

  .drip-clearfix:after {
    visibility: hidden;
    display: block;
    font-size: 0;
    content: " ";
    clear: both;
    height: 0;
  }
  * html .drip-clearfix             { zoom: 1; } /* IE6 */
  *:first-child+html .drip-clearfix { zoom: 1; } /* IE7 */

  /* === Backdrop === */

  .drip-backdrop {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 10000;
    background-color: #000;
    opacity: 0;
    -webkit-transition: opacity .3s linear;
       -moz-transition: opacity .3s linear;
         -o-transition: opacity .3s linear;
            transition: opacity .3s linear;
  }

  .drip-backdrop.drip-in {
    opacity: 0.2;
  }

  .drip-backdrop.drip-hidden {
    display: none;
  }

  /* === Main Container === */

  .drip-lightbox-wrapper * {
    box-sizing: content-box;
  }

  /* === Content === */

  .drip-lightbox .drip-content {
    margin: 0 0 0 -190px;
    padding: 0;
    position: fixed;
    width: 380px;
    top: -25%;
    left: 50%;
    font-size: 100%;
    z-index: 11000;
    color: #333;
    vertical-align: baseline;
    background-color: #ffffff;
    opacity: 0;
    -webkit-border-radius: 8px;
       -moz-border-radius: 8px;
            border-radius: 8px;
    -webkit-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
       -moz-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
            box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
    -webkit-transition: opacity .3s linear, top .3s ease-out, bottom 200ms ease-in;
       -moz-transition: opacity .3s linear, top .3s ease-out, bottom 200ms ease-in;;
         -o-transition: opacity .3s linear, top .3s ease-out, bottom 200ms ease-in;;
            transition: opacity .3s linear, top .3s ease-out, bottom 200ms ease-in;;
  }

  .drip-lightbox.drip-in .drip-content {
    top: 15%;
    opacity: 1;
  }

  .drip-lightbox.drip-hidden .drip-content {
    display: none;
  }

  .drip-lightbox.side-image .drip-content {
    margin-left: -325px;
    width: 650px;
  }

  .drip-lightbox.mobile .drip-content {
    margin: 0;
    width: 100%;
    left: 0;
    top: auto;
    -webkit-border-radius: 0;
       -moz-border-radius: 0;
            border-radius: 0;
  }

  .drip-lightbox.mobile.drip-in .drip-content {
    top: auto;
    bottom: 0;
  }

  .drip-lightbox.drip-scrollable .drip-content {
    overflow-y: scroll;
  }

  /* === Teaser === */

  .drip-lightbox .drip-header h2 {
    display: block;
    margin: 0 !important;
    padding: 12px 0 !important;
    font-size: 14px !important;
    line-height: 13px !important;
    font-weight: bold !important;
    color: #fff !important;
    letter-spacing: 0 !important;
  }

  /* === Panel === */

  .drip-lightbox .drip-content > div.drip-panel {
    padding: 25px;
    background-color: #fff;
    -webkit-border-radius: 6px;
       -moz-border-radius: 6px;
            border-radius: 6px;
  }

  /* === Powered By === */

  .drip-lightbox .drip-powered-by {
    padding: 8px;
    text-align: left;
    font-weight: normal;
    font-size: 10px;
    line-height: 16px;
    color: #A8ACB9;
    text-align: right;
    margin-right: 25px;
    text-transform: uppercase;
    display: -webkit-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }

  .drip-lightbox .drip-powered-by a {
    color: #A8ACB9 !important;
    text-decoration: underline !important;
    margin-left: 6px;
  }

  /* === Content Sections === */

  .drip-lightbox.side-image .drip-form-aside {
    width: 245px;
    text-align: center;
  }

  .drip-lightbox.image-left .drip-form-main {
    margin-left: 270px;
  }

  .drip-lightbox.image-right .drip-form-main {
    margin-right: 270px;
  }

  .drip-lightbox.image-left .drip-form-aside {
    float: left;
  }

  .drip-lightbox.image-right .drip-form-aside {
    float: right;
  }

  @media screen and (max-width: 650px) {
    /* prevent overriding mobile class styles */
    .drip-lightbox.side-image:not(.mobile) .drip-content {
      margin-left: -190px;
      width: 380px;
    }

    .drip-lightbox.side-image .drip-form-main {
      margin-left: 0;
      margin-right: 0;
    }

    .drip-lightbox.side-image .drip-form-aside {
      display: none;
    }
  }

  /* === Content Headings & Paragraphs === */

  .drip-lightbox .drip-content h3 {
    display: block;
    margin: 0 20px 0 0 !important;
    padding: 0 0 15px 0 !important;
    line-height: 1.4 !important;
    font-weight: bold !important;
    text-align: left !important;
    color: #4477bd !important;
    clear: none !important;
  }

  .drip-lightbox .drip-content .drip-description {
    margin: 0;
    padding: 0 0 20px 0;
    line-height: 1.6;
    text-align: left;
  }

  .drip-lightbox .drip-content .drip-post-submission {
    padding: 0;
  }

  .drip-lightbox .drip-content .drip-description a {
    text-decoration: underline;
  }

  .drip-lightbox .drip-content .drip-description em {
    font-style: italic;
  }

  .drip-lightbox .drip-content .drip-description ul,
  .drip-lightbox .drip-content .drip-description ol {
    list-style-position: outside;
    margin: 8px 0 8px 30px;
  }

  .drip-lightbox .drip-content .drip-description ul li
  .drip-lightbox .drip-content .drip-description ol li {
    padding: 0;
  }

  .drip-lightbox .drip-content img.drip-image {
    margin-bottom: 20px;
  }

  .drip-lightbox .drip-content .drip-image-center-helper {
    display: inline-block;
    height: 100%;
    vertical-align: middle;
  }

  .drip-lightbox .drip-content img.drip-image {
    max-width: 245px;
    vertical-align: middle;
  }

  .drip-lightbox .drip-content a.drip-close {
    position: absolute;
    right: 25px;
    top: 25px;
  }

  .drip-lightbox .drip-content a.drip-close:hover {
    cursor: pointer;
  }

  /* === Content Subscribe Form === */

  .drip-lightbox form {
    margin: 0 !important;
    padding: 0 !important;
  }

  .drip-lightbox dl {
    display: block;
    margin: 0;
    padding: 0 0 5px 0;
  }

  .drip-lightbox dl dt {
    display: block;
    padding: 0 0 5px 0;
    /* font-size: 13px; */
    font-weight: bold;
  }

  .drip-lightbox dl.no-labels dt {
    display: none;
  }

  .drip-lightbox dl dd {
    display: block;
    padding: 0 0 8px 0;
  }

  .drip-lightbox .drip-text-field {
    margin: 0 !important;
    padding: 10px 12px !important;
    height: auto !important;
    width: 100% !important;
    color: #4F5362 !important;
    background-color: #fff !important;
    border: 1px solid #A8ACB9 !important;
    -webkit-border-radius: 3px !important;
       -moz-border-radius: 3px !important;
            border-radius: 3px !important;
    -webkit-box-sizing: border-box !important;
       -moz-box-sizing: border-box !important;
        -ms-box-sizing: border-box !important;
            box-sizing: border-box !important;
    background-image: none !important;
    min-width: 0 !important;
    min-height: 0 !important;
  }

  .drip-lightbox .drip-text-field:focus {
    border-color: #9398a9 !important;
    outline: 0;
    background-image: none;
    background-color: #fff !important;
  }

  .drip-lightbox.mobile .drip-text-field {
    font-size: 16px;
  }

  .drip-lightbox .drip-errors {
    padding: 5px 0 0 0;
    font-weight: normal;
    color: red;
  }

  .drip-lightbox .drip-submit-button {
    padding: 6px 26px !important;
    color: #ffffff !important;
    font-weight: bold !important;
    line-height: 1.6 !important;
    border: 0 !important;
    -webkit-border-radius: 3px !important;
       -moz-border-radius: 3px !important;
            border-radius: 3px !important;
    cursor: pointer !important;
    background-image: none !important;
    min-width: 0 !important;
    min-height: 0 !important;
    height: auto;
    transition: background 0.2s ease !important;
    -webkit-box-shadow: 0px 2px 4px rgba(0,0,0,0.20);
       -moz-box-shadow: 0px 2px 4px rgba(0,0,0,0.20);
            box-shadow: 0px 2px 4px rgba(0,0,0,0.20);
  }

  .drip-lightbox .drip-submit-button:hover {
    background-image: none !important;
  }

  .drip-lightbox .drip-submit-button:active {
    background-image: none !important;
  }

  /* checkbox */

  .drip-lightbox input,
  .drip-lightbox textarea {
    display: block;
    box-shadow: none;
    position: relative;
    border: 1px solid #cccccc;
    outline: none;
    border-radius: 3px;
    font: inherit;
    color: #262626;
    padding: 12px 18px;
    transition: border-color 300ms;
    width: 100%;
  }

  .drip-lightbox .zenput--checkbox.hidden {
    margin-bottom: -8px;
    display: none;
  }

  .drip-lightbox .zenput--checkbox input[type="checkbox"] {
    height: 0;
    width: 0;
    opacity: 0;
    position: absolute;
    top: 0;
    left: 0;
  }

  .drip-lightbox .zenput--checkbox input[type="checkbox"] ~ .zenput__checkbox-label {
    font: inherit;
    font-size: 16px;
    line-height: 30px;
    color: #262626;
    cursor: pointer;
    white-space: normal;
    word-break: break-word;
    display: block;
    padding-left: 36px;
    position: relative;
    transition: color 300ms
  }

  .drip-lightbox .zenput--checkbox input[type="checkbox"] ~ .zenput__checkbox-label .zenput__checkbox-label__icon {
    content: "";
    display: block;
    background: #f5f5f5;
    width: 24px;
    height: 24px;
    position: absolute;
    top: 3px;
    left: 0;
    border-radius: 3px;
    border: 1px solid #cccccc;
    box-sizing: border-box;
    padding: 3px;
    transition: background 300ms ease-out, border-color 300ms;
  }

  .drip-lightbox .zenput--checkbox input[type="checkbox"] ~ .zenput__checkbox-label .zenput__checkbox-label__icon svg {
    opacity: 0;
    width: 16px;
    display: block;
    fill: #cccccc;
    transition: opacity 300ms ease-out;
  }

  .drip-lightbox .zenput--checkbox .zenput__checkbox-label .zenput__checkbox-label__icon .octicon-dash {
    display: none;
  }

  .drip-lightbox .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label {
    color: #333 !important;
  }
  .drip-lightbox .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label .zenput__checkbox-label__icon {
    background-color: #ffffff;
    border-color: #a8acb9;
  }
  .drip-lightbox .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label .zenput__checkbox-label__icon svg {
    fill: #f9a82f !important;
    opacity: 1;
  }
  /* stylelint-enable */

</style><style type="text/css">
  /* === Form-Specific Styles === */
  /* stylelint-disable */

  #drip-108599 {
    background: #fff !important;
  }

  #drip-108599 .drip-content h3 {
    color: #f9a82f !important;
    font-size: 28px !important;
  }

  #drip-108599 .drip-submit-button {
    background-color: #f9a82f !important;
    font-size: 19px !important;
  }

  #drip-108599 .drip-submit-button:hover {
    background-color: #eda02d !important;
  }

  #drip-108599 .drip-submit-button:active {
    background-color: #e0972a !important;
  }

  #drip-108599 dl dt,
  #drip-108599 .drip-content .drip-description,
  #drip-108599 .drip-errors {
    font-size: 16px !important;
  }

  #drip-108599 .drip-text-field {
    font-size: 16px !important;
  }

  /* === Reset styles === */

  .drip-lightbox h1,
  .drip-lightbox h2,
  .drip-lightbox h3,
  .drip-lightbox div,
  .drip-lightbox dl,
  .drip-lightbox dt,
  .drip-lightbox dd,
  .drip-lightbox p,
  .drip-lightbox a,
  .drip-lightbox .drip-text-field,
  .drip-lightbox .drip-text-field:focus,
  .drip-lightbox .drip-submit-button {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
    float: none;
    width: auto;
    background-image: none;
    letter-spacing: 0;
    -webkit-box-shadow: none;
       -moz-box-shadow: none;
            box-shadow: none;
    -webkit-text-shadow: none !important;
       -moz-text-shadow: none !important;
            text-shadow: none !important;
  }

  .drip-lightbox a {
    text-decoration: none;
    color: #f9a82f !important;
  }

  .drip-lightbox :focus {
    outline: 0;
  }

  .drip-lightbox input::-webkit-input-placeholder { /* WebKit browsers */
    color: #A8ACB9 !important;
  }
  .drip-lightbox input:-moz-placeholder { /* Mozilla Firefox 4 to 18 */
    color: #A8ACB9 !important;
  }
  .drip-lightbox input::-moz-placeholder { /* Mozilla Firefox 19+ */
    color: #A8ACB9 !important;
  }
  .drip-lightbox input:-ms-input-placeholder { /* Internet Explorer 10+ */
    color: #A8ACB9 !important;
  }

  /* === Clearfix === */

  .drip-clearfix:after {
    visibility: hidden;
    display: block;
    font-size: 0;
    content: " ";
    clear: both;
    height: 0;
  }
  * html .drip-clearfix             { zoom: 1; } /* IE6 */
  *:first-child+html .drip-clearfix { zoom: 1; } /* IE7 */

  /* === Backdrop === */

  .drip-backdrop {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 10000;
    background-color: #000;
    opacity: 0;
    -webkit-transition: opacity .3s linear;
       -moz-transition: opacity .3s linear;
         -o-transition: opacity .3s linear;
            transition: opacity .3s linear;
  }

  .drip-backdrop.drip-in {
    opacity: 0.2;
  }

  .drip-backdrop.drip-hidden {
    display: none;
  }

  /* === Main Container === */

  .drip-lightbox-wrapper * {
    box-sizing: content-box;
  }

  /* === Content === */

  .drip-lightbox .drip-content {
    margin: 0 0 0 -190px;
    padding: 0;
    position: fixed;
    width: 380px;
    top: -25%;
    left: 50%;
    font-size: 100%;
    z-index: 11000;
    color: #333;
    vertical-align: baseline;
    background-color: #ffffff;
    opacity: 0;
    -webkit-border-radius: 8px;
       -moz-border-radius: 8px;
            border-radius: 8px;
    -webkit-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
       -moz-box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
            box-shadow: 0px 10px 28px rgba(0,0,0,0.36);
    -webkit-transition: opacity .3s linear, top .3s ease-out, bottom 200ms ease-in;
       -moz-transition: opacity .3s linear, top .3s ease-out, bottom 200ms ease-in;;
         -o-transition: opacity .3s linear, top .3s ease-out, bottom 200ms ease-in;;
            transition: opacity .3s linear, top .3s ease-out, bottom 200ms ease-in;;
  }

  .drip-lightbox.drip-in .drip-content {
    top: 15%;
    opacity: 1;
  }

  .drip-lightbox.drip-hidden .drip-content {
    display: none;
  }

  .drip-lightbox.side-image .drip-content {
    margin-left: -325px;
    width: 650px;
  }

  .drip-lightbox.mobile .drip-content {
    margin: 0;
    width: 100%;
    left: 0;
    top: auto;
    -webkit-border-radius: 0;
       -moz-border-radius: 0;
            border-radius: 0;
  }

  .drip-lightbox.mobile.drip-in .drip-content {
    top: auto;
    bottom: 0;
  }

  .drip-lightbox.drip-scrollable .drip-content {
    overflow-y: scroll;
  }

  /* === Teaser === */

  .drip-lightbox .drip-header h2 {
    display: block;
    margin: 0 !important;
    padding: 12px 0 !important;
    font-size: 14px !important;
    line-height: 13px !important;
    font-weight: bold !important;
    color: #fff !important;
    letter-spacing: 0 !important;
  }

  /* === Panel === */

  .drip-lightbox .drip-content > div.drip-panel {
    padding: 25px;
    background-color: #fff;
    -webkit-border-radius: 6px;
       -moz-border-radius: 6px;
            border-radius: 6px;
  }

  /* === Powered By === */

  .drip-lightbox .drip-powered-by {
    padding: 8px;
    text-align: left;
    font-weight: normal;
    font-size: 10px;
    line-height: 16px;
    color: #A8ACB9;
    text-align: right;
    margin-right: 25px;
    text-transform: uppercase;
    display: -webkit-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }

  .drip-lightbox .drip-powered-by a {
    color: #A8ACB9 !important;
    text-decoration: underline !important;
    margin-left: 6px;
  }

  /* === Content Sections === */

  .drip-lightbox.side-image .drip-form-aside {
    width: 245px;
    text-align: center;
  }

  .drip-lightbox.image-left .drip-form-main {
    margin-left: 270px;
  }

  .drip-lightbox.image-right .drip-form-main {
    margin-right: 270px;
  }

  .drip-lightbox.image-left .drip-form-aside {
    float: left;
  }

  .drip-lightbox.image-right .drip-form-aside {
    float: right;
  }

  @media screen and (max-width: 650px) {
    /* prevent overriding mobile class styles */
    .drip-lightbox.side-image:not(.mobile) .drip-content {
      margin-left: -190px;
      width: 380px;
    }

    .drip-lightbox.side-image .drip-form-main {
      margin-left: 0;
      margin-right: 0;
    }

    .drip-lightbox.side-image .drip-form-aside {
      display: none;
    }
  }

  /* === Content Headings & Paragraphs === */

  .drip-lightbox .drip-content h3 {
    display: block;
    margin: 0 20px 0 0 !important;
    padding: 0 0 15px 0 !important;
    line-height: 1.4 !important;
    font-weight: bold !important;
    text-align: left !important;
    color: #4477bd !important;
    clear: none !important;
  }

  .drip-lightbox .drip-content .drip-description {
    margin: 0;
    padding: 0 0 20px 0;
    line-height: 1.6;
    text-align: left;
  }

  .drip-lightbox .drip-content .drip-post-submission {
    padding: 0;
  }

  .drip-lightbox .drip-content .drip-description a {
    text-decoration: underline;
  }

  .drip-lightbox .drip-content .drip-description em {
    font-style: italic;
  }

  .drip-lightbox .drip-content .drip-description ul,
  .drip-lightbox .drip-content .drip-description ol {
    list-style-position: outside;
    margin: 8px 0 8px 30px;
  }

  .drip-lightbox .drip-content .drip-description ul li
  .drip-lightbox .drip-content .drip-description ol li {
    padding: 0;
  }

  .drip-lightbox .drip-content img.drip-image {
    margin-bottom: 20px;
  }

  .drip-lightbox .drip-content .drip-image-center-helper {
    display: inline-block;
    height: 100%;
    vertical-align: middle;
  }

  .drip-lightbox .drip-content img.drip-image {
    max-width: 245px;
    vertical-align: middle;
  }

  .drip-lightbox .drip-content a.drip-close {
    position: absolute;
    right: 25px;
    top: 25px;
  }

  .drip-lightbox .drip-content a.drip-close:hover {
    cursor: pointer;
  }

  /* === Content Subscribe Form === */

  .drip-lightbox form {
    margin: 0 !important;
    padding: 0 !important;
  }

  .drip-lightbox dl {
    display: block;
    margin: 0;
    padding: 0 0 5px 0;
  }

  .drip-lightbox dl dt {
    display: block;
    padding: 0 0 5px 0;
    /* font-size: 13px; */
    font-weight: bold;
  }

  .drip-lightbox dl.no-labels dt {
    display: none;
  }

  .drip-lightbox dl dd {
    display: block;
    padding: 0 0 8px 0;
  }

  .drip-lightbox .drip-text-field {
    margin: 0 !important;
    padding: 10px 12px !important;
    height: auto !important;
    width: 100% !important;
    color: #4F5362 !important;
    background-color: #fff !important;
    border: 1px solid #A8ACB9 !important;
    -webkit-border-radius: 3px !important;
       -moz-border-radius: 3px !important;
            border-radius: 3px !important;
    -webkit-box-sizing: border-box !important;
       -moz-box-sizing: border-box !important;
        -ms-box-sizing: border-box !important;
            box-sizing: border-box !important;
    background-image: none !important;
    min-width: 0 !important;
    min-height: 0 !important;
  }

  .drip-lightbox .drip-text-field:focus {
    border-color: #9398a9 !important;
    outline: 0;
    background-image: none;
    background-color: #fff !important;
  }

  .drip-lightbox.mobile .drip-text-field {
    font-size: 16px;
  }

  .drip-lightbox .drip-errors {
    padding: 5px 0 0 0;
    font-weight: normal;
    color: red;
  }

  .drip-lightbox .drip-submit-button {
    padding: 6px 26px !important;
    color: #ffffff !important;
    font-weight: bold !important;
    line-height: 1.6 !important;
    border: 0 !important;
    -webkit-border-radius: 3px !important;
       -moz-border-radius: 3px !important;
            border-radius: 3px !important;
    cursor: pointer !important;
    background-image: none !important;
    min-width: 0 !important;
    min-height: 0 !important;
    height: auto;
    transition: background 0.2s ease !important;
    -webkit-box-shadow: 0px 2px 4px rgba(0,0,0,0.20);
       -moz-box-shadow: 0px 2px 4px rgba(0,0,0,0.20);
            box-shadow: 0px 2px 4px rgba(0,0,0,0.20);
  }

  .drip-lightbox .drip-submit-button:hover {
    background-image: none !important;
  }

  .drip-lightbox .drip-submit-button:active {
    background-image: none !important;
  }

  /* checkbox */

  .drip-lightbox input,
  .drip-lightbox textarea {
    display: block;
    box-shadow: none;
    position: relative;
    border: 1px solid #cccccc;
    outline: none;
    border-radius: 3px;
    font: inherit;
    color: #262626;
    padding: 12px 18px;
    transition: border-color 300ms;
    width: 100%;
  }

  .drip-lightbox .zenput--checkbox.hidden {
    margin-bottom: -8px;
    display: none;
  }

  .drip-lightbox .zenput--checkbox input[type="checkbox"] {
    height: 0;
    width: 0;
    opacity: 0;
    position: absolute;
    top: 0;
    left: 0;
  }

  .drip-lightbox .zenput--checkbox input[type="checkbox"] ~ .zenput__checkbox-label {
    font: inherit;
    font-size: 16px;
    line-height: 30px;
    color: #262626;
    cursor: pointer;
    white-space: normal;
    word-break: break-word;
    display: block;
    padding-left: 36px;
    position: relative;
    transition: color 300ms
  }

  .drip-lightbox .zenput--checkbox input[type="checkbox"] ~ .zenput__checkbox-label .zenput__checkbox-label__icon {
    content: "";
    display: block;
    background: #f5f5f5;
    width: 24px;
    height: 24px;
    position: absolute;
    top: 3px;
    left: 0;
    border-radius: 3px;
    border: 1px solid #cccccc;
    box-sizing: border-box;
    padding: 3px;
    transition: background 300ms ease-out, border-color 300ms;
  }

  .drip-lightbox .zenput--checkbox input[type="checkbox"] ~ .zenput__checkbox-label .zenput__checkbox-label__icon svg {
    opacity: 0;
    width: 16px;
    display: block;
    fill: #cccccc;
    transition: opacity 300ms ease-out;
  }

  .drip-lightbox .zenput--checkbox .zenput__checkbox-label .zenput__checkbox-label__icon .octicon-dash {
    display: none;
  }

  .drip-lightbox .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label {
    color: #333 !important;
  }
  .drip-lightbox .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label .zenput__checkbox-label__icon {
    background-color: #ffffff;
    border-color: #a8acb9;
  }
  .drip-lightbox .zenput--checkbox input[type="checkbox"]:checked ~ .zenput__checkbox-label .zenput__checkbox-label__icon svg {
    fill: #f9a82f !important;
    opacity: 1;
  }
  /* stylelint-enable */

</style><link rel="prefetch" href="https://tpc.googlesyndication.com/safeframe/1-0-37/html/container.html"></head>
<body>
<nav class="navbar fixed-top navbar-expand-lg navbar-dark flex-column">
<div class="container flex-row">
<a class="navbar-brand" href="https://realpython.com/">
<img src="./Request_files/real-python-logo.893c30edea53.svg" height="40" class="d-inline-block align-top" alt="Real Python">
</a>
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="navbarSupportedContent">
<ul class="navbar-nav mr-2 flex-fill">
<li class="nav-item">
<a class="nav-link" href="https://realpython.com/start-here/">Start&nbsp;Here</a>
</li>
<li class="nav-item dropdown">
<a class="nav-link dropdown-toggle" href="https://realpython.com/python-interface/#" id="navbarDropdownLibrary" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
<span class="fa fa-graduation-cap"></span> Learn Python
</a>
<div class="dropdown-menu" aria-labelledby="navbarDropdownLibrary">
<a class="dropdown-item" href="https://realpython.com/" style="color: #ff7e73; line-height: 110%;"><i class="fa fa-fw mr-1 fa-graduation-cap"></i> Python Tutorials →<br><small class="text-secondary">In-depth articles and tutorials</small></a>
<a class="dropdown-item" href="https://realpython.com/courses/" style="color: #abe5b1; line-height: 110%;"><i class="fa fa-fw mr-1 fa-film"></i> Video Courses →<br><small class="text-secondary">Step-by-step video lessons</small></a>
<a class="dropdown-item" href="https://realpython.com/quizzes/" style="color: #abe0e5; line-height: 110%;"><i class="fa fa-fw mr-1 fa-trophy"></i> Quizzes →<br><small class="text-secondary">Check your learning progress</small></a>
<a class="dropdown-item" href="https://realpython.com/learning-paths/" style="color: #ffc873; line-height: 110%;"><i class="fa fa-fw mr-1 fa-map-o"></i> Learning Paths →<br><small class="text-secondary">Guided study plans for accelerated learning</small></a>
<a class="dropdown-item" href="https://realpython.com/community/" style="color: #e5c6ab; line-height: 110%;"><i class="fa fa-fw mr-1 fa-slack"></i> Community →<br><small class="text-secondary">Learn with other Pythonistas</small></a>
<a class="dropdown-item pb-3" href="https://realpython.com/tutorials/all/" style="color: #b8abe5; line-height: 110%;"><i class="fa fa-fw mr-1 fa-tags"></i> Topics →<br><small class="text-secondary">Focus on a specific area or skill level</small></a>
<a class="dropdown-item border-top" href="https://realpython.com/account/join/"><i class="fa fa-fw fa-star text-warning"></i> Unlock All Content</a>
</div>
</li>
<li class="nav-item dropdown">
<a class="nav-link dropdown-toggle" href="https://realpython.com/python-interface/#" id="navbarDropdownBooksCourses" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
Store
</a>
<div class="dropdown-menu" aria-labelledby="navbarDropdownBooksCourses">
<a class="dropdown-item" href="https://realpython.com/account/join/"><i class="fa fa-fw fa-star text-warning"></i> RP Membership</a>
<a class="dropdown-item" href="https://realpython.com/products/python-basics-book/">Python Basics Book</a>
<a class="dropdown-item" href="https://realpython.com/products/python-tricks-book/">Python Tricks Book</a>
<a class="dropdown-item" href="https://realpython.com/products/real-python-course/">The Real Python Course</a>
<a class="dropdown-item" href="https://realpython.com/products/managing-python-dependencies/">Managing Python Dependencies</a>
<a class="dropdown-item" href="https://realpython.com/products/sublime-python/">Sublime Text + Python Setup</a>
<a class="dropdown-item" href="https://realpython.com/products/pythonic-wallpapers/">Pythonic Wallpapers Pack</a>
<a class="dropdown-item" href="https://nerdlettering.com/" target="_blank">Python Mugs, T-Shirts, and More</a>
<a class="dropdown-item" href="https://www.pythonistacafe.com/" target="_blank">Pythonista Cafe Community</a>
<a class="dropdown-item border-top" href="https://realpython.com/products/">Browse All »</a>
</div>
</li>
<li class="nav-item dropdown">
<a class="nav-link dropdown-toggle" href="https://realpython.com/python-interface/#" id="navbarDropdownMore" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
More
</a>
<div class="dropdown-menu" aria-labelledby="navbarDropdownMore">
<a class="dropdown-item" href="https://realpython.com/newsletter/">Python Newsletter</a>
<a class="dropdown-item" href="https://realpython.com/podcasts/rpp/">Python Podcast</a>
<a class="dropdown-item" href="https://www.pythonjobshq.com/" target="_blank">Python Job Board</a>
<a class="dropdown-item" href="https://realpython.com/team/">Meet the Team</a>
<a class="dropdown-item" href="https://realpython.com/write-for-us/">Become a Tutorial Author</a>
<a class="dropdown-item" href="https://realpython.com/become-an-instructor/">Become a Video Instructor</a>
</div>
</li>
</ul>
<div class="d-block d-xl-none">
<ul class="navbar-nav">
<li class="nav-item">
<a class="nav-link" href="https://realpython.com/search" title="Search"><span class="d-block d-lg-none"><i class="fa fa-search"></i> Search</span><span class="d-none d-lg-block"><i class="fa fa-search"></i></span></a>
</li>
</ul>
 </div>
<div class="d-none d-xl-block">
<form class="form-inline my-2 my-lg-0 mr-2 flex-fill" action="https://realpython.com/search" method="GET">
<input class="search-field form-control form-control-md mr-sm-1 mr-lg-2 w-100" type="search" placeholder="Search…" aria-label="Search" name="q">
</form>
</div>
<ul class="navbar-nav">
<li class="nav-item form-inline">
<a class="ml-2 ml-lg-0 btn btn-sm btn-primary px-3" href="https://realpython.com/account/join/">Join</a>
</li>
<li class="nav-item">
<a class="btn text-light" href="https://realpython.com/account/login/">Sign‑In</a>
</li>
</ul>
</div>
</div>
<div class="flex-row w-100" style="border-top: 1px dashed #ffc107 !important;">
<div class="container">
<a class="link-unstyled mx-auto" href="https://realpython.com/podcasts/rpp/"><p class="my-1 small"><span class="text-warning"><span class="fa fa-podcast mr-1"></span><strong>The Real Python Podcast Is Here:</strong> Python Tips, Interviews, and More →</span></p></a>
</div>
</div>
</nav>
<div class="container main-content">
<div class="row justify-content-center">
<div class="col-md-11 col-lg-8 article">
<figure class="embed-responsive embed-responsive-16by9">
<img class="card-img-top m-0 p-0 embed-responsive-item rounded" style="object-fit: contain;" alt="Implementing an Interface in Python" src="./Request_files/Interfaces-in-Python_Watermarked.f9ce5bda238c.jpg" width="1920" height="1080" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/Interfaces-in-Python_Watermarked.f9ce5bda238c.jpg&amp;w=480&amp;sig=04ee32a1dd9ba53b36d1c5092f778c42627a7738 480w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/Interfaces-in-Python_Watermarked.f9ce5bda238c.jpg&amp;w=960&amp;sig=7e61f7c3a91eb150a262bb519827506a0ceef654 960w, https://files.realpython.com/media/Interfaces-in-Python_Watermarked.f9ce5bda238c.jpg 1920w" sizes="75vw">
</figure>
<h1>Implementing an Interface in Python</h1>
<p class="mb-0">
<span class="text-muted">by <a class="text-muted" href="https://realpython.com/python-interface/#author">William Murphy</a>
<span class="ml-2 fa fa-clock-o"></span> Feb 10, 2020
<span class="ml-2 mr-1 fa fa-comments"></span><a class="text-muted" href="https://realpython.com/python-interface/#reader-comments"><span class="disqus-comment-count" data-disqus-identifier="https://realpython.com/python-interface/">16 Comments</span></a>
<span class="ml-2 fa fa-tags"></span>
<a href="https://realpython.com/tutorials/advanced/" class="badge badge-light text-muted">advanced</a>
<a href="https://realpython.com/tutorials/python/" class="badge badge-light text-muted">python</a>
</span></p><div class="d-flex flex-row justify-content-between my-2">
<div class="align-self-center">
<span>
<a target="_blank" rel="nofollow" href="https://twitter.com/intent/tweet/?text=Check%20out%20this%20%23Python%20tutorial:%20Implementing%20an%20Interface%20in%20Python%20by%20@realpython&amp;url=https%3A//realpython.com/python-interface/" class="mr-1 badge badge-twitter text-light mb-1"><i class="mr-1 fa fa-twitter text-light"></i>Tweet</a>
<a target="_blank" rel="nofollow" href="https://facebook.com/sharer/sharer.php?u=https%3A//realpython.com/python-interface/" class="mr-1 badge badge-facebook text-light mb-1"><i class="mr-1 fa fa-facebook text-light"></i>Share</a>
<a target="_blank" rel="nofollow" href="mailto:?subject=Python%20article%20for%20you&amp;body=Check%20out%20this%20Python%20tutorial:%0A%0AImplementing%20an%20Interface%20in%20Python%0A%0Ahttps%3A//realpython.com/python-interface/" class="mr-1 badge badge-red text-light mb-1"><i class="mr-1 fa fa-envelope text-light"></i>Email</a>
</span>
</div>
</div>
<p></p>
<div class="article-body">
<div class="bg-light sidebar-module sidebar-module-inset" id="toc">
<p class="h3 mb-2 text-muted">Table of Contents</p>
<div class="toc">
<ul>
<li><a href="https://realpython.com/python-interface/#python-interface-overview">Python Interface Overview</a></li>
<li><a href="https://realpython.com/python-interface/#informal-interfaces">Informal Interfaces</a><ul>
<li><a href="https://realpython.com/python-interface/#using-metaclasses">Using Metaclasses</a></li>
<li><a href="https://realpython.com/python-interface/#using-virtual-base-classes">Using Virtual Base Classes</a></li>
</ul>
</li>
<li><a href="https://realpython.com/python-interface/#formal-interfaces">Formal Interfaces</a><ul>
<li><a href="https://realpython.com/python-interface/#using-abcabcmeta">Using abc.ABCMeta</a></li>
<li><a href="https://realpython.com/python-interface/#using-__subclasshook__">Using .__subclasshook__()</a></li>
<li><a href="https://realpython.com/python-interface/#using-abc-to-register-a-virtual-subclass">Using abc to Register a Virtual Subclass</a></li>
<li><a href="https://realpython.com/python-interface/#using-subclass-detection-with-registration">Using Subclass Detection With Registration</a></li>
<li><a href="https://realpython.com/python-interface/#using-abstract-method-declaration">Using Abstract Method Declaration</a></li>
</ul>
</li>
<li><a href="https://realpython.com/python-interface/#interfaces-in-other-languages">Interfaces in Other Languages</a><ul>
<li><a href="https://realpython.com/python-interface/#java">Java</a></li>
<li><a href="https://realpython.com/python-interface/#c">C++</a></li>
<li><a href="https://realpython.com/python-interface/#go">Go</a></li>
</ul>
</li>
<li><a href="https://realpython.com/python-interface/#conclusion">Conclusion</a></li>
</ul>
</div>
</div>
<div class="sidebar-module sidebar-module-inset p-0" style="overflow:hidden;">
<div style="display:block;position:relative;">
<div style="display:block;width:100%;padding-top:12.5%;"></div>
<div class="rpad" data-unit="8x1" style="position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;"><a href="https://srv.realpython.net/click/36956403387/?c=50370534298&amp;p=58946116052&amp;r=59969" rel="nofollow" target="_blank"><img src="./Request_files/e1ba3fda38afbf853a398cfa81ae1bca" style="max-width: 100%; max-height: 100%; width: 100%;"></a></div>
</div>
</div>
<p>Interfaces play an important role in software engineering. As an application grows, updates and changes to the code base become more difficult to manage. More often than not, you wind up having classes that look very similar but are unrelated, which can lead to some confusion. In this tutorial, you’ll see how you can use a <strong>Python interface</strong> to help determine what class you should use to tackle the current problem.</p>
<p><strong>In this tutorial, you’ll be able to:</strong></p>
<ul>
<li><strong>Understand</strong> how interfaces work and the caveats of Python interface creation</li>
<li><strong>Comprehend</strong> how useful interfaces are in a dynamic language like Python</li>
<li><strong>Implement</strong> an informal Python interface</li>
<li><strong>Use</strong> <code>abc.ABCMeta</code> and <code>@abc.abstractmethod</code> to implement a formal Python interface</li>
</ul>
<p>Interfaces in Python are handled differently than in most other languages, and they can vary in their design complexity. By the end of this tutorial, you’ll have a better understanding of some aspects of Python’s data model, as well as how interfaces in Python compare to those in languages like Java, C++, and Go.</p>
<div class="alert alert-warning" role="alert"><p><strong>Free Bonus:</strong> <a href="https://realpython.com/python-interface/" class="alert-link" data-toggle="modal" data-target="#modal-python-mastery-course" data-focus="false">5 Thoughts On Python Mastery</a>, a free course for Python developers that shows you the roadmap and the mindset you'll need to take your Python skills to the next level.</p></div>
<div class="w-100 text-center js-needs-scaling" style="transform-origin: 0 0;"><div id="waldo-tag-4996" data-processed="true" data-google-query-id="CM7Ny6fVsegCFZEcgQodLZsERQ"><div id="google_ads_iframe_/124067137/realpython728x90FS_1_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/124067137/realpython728x90FS_1_0" title="3rd party ad content" name="google_ads_iframe_/124067137/realpython728x90FS_1_0" width="480" height="320" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" data-google-container-id="1" style="border: 0px; vertical-align: bottom;" data-load-complete="true" src="./Request_files/saved_resource.html"></iframe></div></div> <a class="small text-muted js-disclosure" href="https://realpython.com/account/join/" rel="nofollow" style=""> <i aria-hidden="true" class="fa fa-info-circle"> </i> Remove ads</a></div><h2 id="python-interface-overview">Python Interface Overview</h2>
<p>At a high level, an interface acts as a <strong>blueprint</strong> for designing classes. Like classes, interfaces define methods. Unlike classes, these methods are abstract. An <strong>abstract method</strong> is one that the interface simply defines. It doesn’t implement the methods. This is done by classes, which then <strong>implement</strong> the interface and give concrete meaning to the interface’s abstract methods.</p>
<p>Python’s approach to interface design is somewhat different when compared to languages like <a href="https://realpython.com/oop-in-python-vs-java/">Java</a>, Go, and C++. These languages all have an <code>interface</code> keyword, while Python does not. Python further deviates from other languages in one other aspect. It doesn’t require the class that’s implementing the interface to define all of the interface’s abstract methods.</p>
<h2 id="informal-interfaces">Informal Interfaces</h2>
<p>In certain circumstances, you may not need the strict rules of a formal Python interface. Python’s dynamic nature allows you to implement an <strong>informal interface</strong>. An informal Python interface is a class that defines methods that can be overridden, but there’s no strict enforcement.</p>
<p>In the following example, you’ll take the perspective of a data engineer who needs to extract text from various different unstructured file types, like PDFs and emails. You’ll create an informal interface that defines the methods that will be in both the <code>PdfParser</code> and <code>EmlParser</code> concrete classes:</p>
<div class="highlight python"><pre><span></span><code><span class="k">class</span> <span class="nc">InformalParserInterface</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Load in the file for extracting text."""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""Extract text from the currently loaded file."""</span>
        <span class="k">pass</span>
</code></pre></div>
<p><code>InformalParserInterface</code> defines the two methods <code>.load_data_source()</code> and <code>.extract_text()</code>. These methods are defined but not implemented. The implementation will occur once you create <strong>concrete classes</strong> that inherit from <code>InformalParserInterface</code>.</p>
<p>As you can see, <code>InformalParserInterface</code> looks identical to a standard Python class. You rely on <a href="https://realpython.com/lessons/duck-typing/">duck typing</a> to inform users that this is an interface and should be used accordingly.</p>
<div class="alert alert-primary" role="alert">
<p><strong>Note:</strong> Haven’t heard of <strong>duck typing</strong>? This term says that if you have an object that looks like a duck, walks like a duck, and quacks like a duck, then it must be a duck! To learn more, check out <a href="https://realpython.com/lessons/duck-typing/">Duck Typing</a>.</p>
</div>
<p>With duck typing in mind, you define two classes that implement the <code>InformalParserInterface</code>. To use your interface, you must create a concrete class. A <strong>concrete class</strong> is a subclass of the interface that provides an implementation of the interface’s methods. You’ll create two concrete classes to implement your interface. The first is <code>PdfParser</code>, which you’ll use to parse the text from PDF files:</p>
<div class="highlight python"><pre><span></span><code><span class="k">class</span> <span class="nc">PdfParser</span><span class="p">(</span><span class="n">InformalParserInterface</span><span class="p">):</span>
    <span class="sd">"""Extract text from a PDF"""</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Overrides InformalParserInterface.load_data_source()"""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""Overrides InformalParserInterface.extract_text()"""</span>
        <span class="k">pass</span>
</code></pre></div>
<p>The concrete implementation of <code>InformalParserInterface</code> now allows you to extract text from PDF files.</p>
<p>The second concrete class is <code>EmlParser</code>, which you’ll use to parse the text from emails:</p>
<div class="highlight python"><pre><span></span><code><span class="k">class</span> <span class="nc">EmlParser</span><span class="p">(</span><span class="n">InformalParserInterface</span><span class="p">):</span>
    <span class="sd">"""Extract text from an email"""</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Overrides InformalParserInterface.load_data_source()"""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text_from_email</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""A method defined only in EmlParser.</span>
<span class="sd">        Does not override InformalParserInterface.extract_text()</span>
<span class="sd">        """</span>
        <span class="k">pass</span>
</code></pre></div>
<p>The concrete implementation of <code>InformalParserInterface</code> now allows you to extract text from email files.</p>
<p>So far, you’ve defined two <strong>concrete implementations</strong> of the <code>InformalPythonInterface</code>. However, note that <code>EmlParser</code> fails to properly define <code>.extract_text()</code>. If you were to check whether <code>EmlParser</code> implements <code>InformalParserInterface</code>, then you’d get the following result:</p>
<div class="highlight python repl"><span class="repl-toggle" title="Toggle REPL prompts and output">&gt;&gt;&gt;</span><pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="c1"># Check if both PdfParser and EmlParser implement InformalParserInterface</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">issubclass</span><span class="p">(</span><span class="n">PdfParser</span><span class="p">,</span> <span class="n">InformalParserInterface</span><span class="p">)</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">issubclass</span><span class="p">(</span><span class="n">EmlParser</span><span class="p">,</span> <span class="n">InformalParserInterface</span><span class="p">)</span>
<span class="go">True</span>
</code></pre></div>
<p>This would return <code>True</code>, which poses a bit of a problem since it violates the definition of an interface!</p>
<p>Now check the <strong>method resolution order (MRO)</strong> of <code>PdfParser</code> and <code>EmlParser</code>. This tells you the superclasses of the class in question, as well as the order in which they’re searched for executing a method. You can view a class’s MRO by using the dunder method <code>cls.__mro__</code>:</p>
<div class="highlight python repl"><span class="repl-toggle" title="Toggle REPL prompts and output">&gt;&gt;&gt;</span><pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">PdfParser</span><span class="o">.</span><span class="vm">__mro__</span>
<span class="go">(__main__.PdfParser, __main__.InformalParserInterface, object)</span>

<span class="gp">&gt;&gt;&gt; </span><span class="n">EmlParser</span><span class="o">.</span><span class="vm">__mro__</span>
<span class="go">(__main__.EmlParser, __main__.InformalParserInterface, object)</span>
</code></pre></div>
<p>Such informal interfaces are fine for small projects where only a few developers are working on the source code. However, as projects get larger and teams grow, this could lead to developers spending countless hours looking for hard-to-find logic errors in the codebase!</p>
<div class="w-100 text-center js-needs-scaling" style="transform-origin: 0 0;"><div id="waldo-tag-4998" data-processed="true" data-google-query-id="CL2aqbvVsegCFRJqwQodNLkHZg"><div id="google_ads_iframe_/124067137/realpython728x90FS_2_0__container__" style="border: 0pt none; display: inline-block; width: 300px; height: 250px;"><iframe frameborder="0" src="./Request_files/container.html" id="google_ads_iframe_/124067137/realpython728x90FS_2_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="300" height="250" data-is-safeframe="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" data-google-container-id="2" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div></div> <a class="small text-muted js-disclosure" href="https://realpython.com/account/join/" rel="nofollow" style=""> <i aria-hidden="true" class="fa fa-info-circle"> </i> Remove ads</a></div><h3 id="using-metaclasses">Using Metaclasses</h3>
<p>Ideally, you would want <code>issubclass(EmlParser, InformalParserInterface</code> to return <code>False</code> when the implementing class doesn’t define all of the interface’s abstract methods. To do this, you’ll create a <a href="https://realpython.com/python-metaclasses/">metaclass</a> called <code>ParserMeta</code>. You’ll be overriding two <a href="https://dbader.org/blog/python-dunder-methods">dunder</a> methods:</p>
<ol>
<li><code>.__instancecheck__()</code></li>
<li><code>.__subclasscheck__()</code></li>
</ol>
<p>In the code block below, you create a class called <code>UpdatedInformalParserInterface</code> that builds from the <code>ParserMeta</code> metaclass:</p>
<div class="highlight python"><pre><span></span><code><span class="k">class</span> <span class="nc">ParserMeta</span><span class="p">(</span><span class="nb">type</span><span class="p">):</span>
    <span class="sd">"""A Parser metaclass that will be used for parser class creation.</span>
<span class="sd">    """</span>
    <span class="k">def</span> <span class="fm">__instancecheck__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">instance</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__subclasscheck__</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">instance</span><span class="p">))</span>

    <span class="k">def</span> <span class="fm">__subclasscheck__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">subclass</span><span class="p">):</span>
        <span class="k">return</span> <span class="p">(</span><span class="nb">hasattr</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="s1">'load_data_source'</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="n">callable</span><span class="p">(</span><span class="n">subclass</span><span class="o">.</span><span class="n">load_data_source</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="nb">hasattr</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="s1">'extract_text'</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="n">callable</span><span class="p">(</span><span class="n">subclass</span><span class="o">.</span><span class="n">extract_text</span><span class="p">))</span>

<span class="k">class</span> <span class="nc">UpdatedInformalParserInterface</span><span class="p">(</span><span class="n">metaclass</span><span class="o">=</span><span class="n">ParserMeta</span><span class="p">):</span>
    <span class="sd">"""This interface is used for concrete classes to inherit from.</span>
<span class="sd">    There is no need to define the ParserMeta methods as any class</span>
<span class="sd">    as they are implicitly made available via .__subclasscheck__().</span>
<span class="sd">    """</span>
    <span class="k">pass</span>
</code></pre></div>
<p>Now that <code>ParserMeta</code> and <code>UpdatedInformalParserInterface</code> have been created, you can create your concrete implementations.</p>
<p>First, create a new class for parsing PDFs called <code>PdfParserNew</code>:</p>
<div class="highlight python"><pre><span></span><code><span class="k">class</span> <span class="nc">PdfParserNew</span><span class="p">:</span>
    <span class="sd">"""Extract text from a PDF."""</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Overrides UpdatedInformalParserInterface.load_data_source()"""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""Overrides UpdatedInformalParserInterface.extract_text()"""</span>
        <span class="k">pass</span>
</code></pre></div>
<p>Here, <code>PdfParserNew</code> overrides <code>.load_data_source()</code> and <code>.extract_text()</code>, so <code>issubclass(PdfParserNew, UpdatedInformalParserInterface)</code> should return <code>True</code>.</p>
<p>In this next code block, you have a new implementation of the email parser called <code>EmlParserNew</code>:</p>
<div class="highlight python"><pre><span></span><code><span class="k">class</span> <span class="nc">EmlParserNew</span><span class="p">:</span>
    <span class="sd">"""Extract text from an email."""</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Overrides UpdatedInformalParserInterface.load_data_source()"""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text_from_email</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""A method defined only in EmlParser.</span>
<span class="sd">        Does not override UpdatedInformalParserInterface.extract_text()</span>
<span class="sd">        """</span>
        <span class="k">pass</span>
</code></pre></div>
<p>Here, you have a metaclass that’s used to create <code>UpdatedInformalParserInterface</code>. By using a metaclass, you don’t need to explicitly define the subclasses. Instead, the subclass must <strong>define the required methods</strong>. If it doesn’t, then <code>issubclass(EmlParserNew, UpdatedInformalParserInterface)</code> will return <code>False</code>.</p>
<p>Running <code>issubclass()</code> on your concrete classes will produce the following:</p>
<div class="highlight python repl"><span class="repl-toggle" title="Toggle REPL prompts and output">&gt;&gt;&gt;</span><pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="nb">issubclass</span><span class="p">(</span><span class="n">PdfParserNew</span><span class="p">,</span> <span class="n">UpdatedInformalParserInterface</span><span class="p">)</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">issubclass</span><span class="p">(</span><span class="n">EmlParserNew</span><span class="p">,</span> <span class="n">UpdatedInformalParserInterface</span><span class="p">)</span>
<span class="go">False</span>
</code></pre></div>
<p>As expected, <code>EmlParserNew</code> is not a subclass of <code>UpdatedInformalParserInterface</code> since <code>.extract_text()</code> wasn’t defined in <code>EmlParserNew</code>.</p>
<p>Now, let’s have a look at the MRO:</p>
<div class="highlight python repl"><span class="repl-toggle" title="Toggle REPL prompts and output">&gt;&gt;&gt;</span><pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">PdfParserNew</span><span class="o">.</span><span class="vm">__mro__</span>
<span class="go">(&lt;class '__main__.PdfParserNew'&gt;, &lt;class 'object'&gt;)</span>
</code></pre></div>
<p>As you can see, <code>UpdatedInformalParserInterface</code> is a superclass of <code>PdfParserNew</code>, but it doesn’t appear in the MRO. This unusual behavior is caused by the fact that <code>UpdatedInformalParserInterface</code> is a <strong>virtual base class</strong> of <code>PdfParserNew</code>.</p>
<h3 id="using-virtual-base-classes">Using Virtual Base Classes</h3>
<p>In the previous example, <code>issubclass(EmlParserNew, UpdatedInformalParserInterface)</code> returned <code>True</code>, even though <code>UpdatedInformalParserInterface</code> did not appear in the <code>EmlParserNew</code> MRO. That’s because <code>UpdatedInformalParserInterface</code> is a <strong>virtual base class</strong> of <code>EmlParserNew</code>. </p>
<p>The key difference between these and standard subclasses is that virtual base classes use the <code>.__subclasscheck__()</code> dunder method to implicitly check if a class is a virtual subclass of the superclass. Additionally, virtual base classes don’t appear in the subclass MRO.</p>
<p>Take a look at this code block:</p>
<div class="highlight python"><pre><span></span><code><span class="k">class</span> <span class="nc">PersonMeta</span><span class="p">(</span><span class="nb">type</span><span class="p">):</span>
    <span class="sd">"""A person metaclass"""</span>
    <span class="k">def</span> <span class="fm">__instancecheck__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">instance</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__subclasscheck__</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">instance</span><span class="p">))</span>

    <span class="k">def</span> <span class="fm">__subclasscheck__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">subclass</span><span class="p">):</span>
        <span class="k">return</span> <span class="p">(</span><span class="nb">hasattr</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="s1">'name'</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="n">callable</span><span class="p">(</span><span class="n">subclass</span><span class="o">.</span><span class="n">name</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="nb">hasattr</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="s1">'age'</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="n">callable</span><span class="p">(</span><span class="n">subclass</span><span class="o">.</span><span class="n">age</span><span class="p">))</span>

<span class="k">class</span> <span class="nc">PersonSuper</span><span class="p">:</span>
    <span class="sd">"""A person superclass"""</span>
    <span class="k">def</span> <span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">age</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">Person</span><span class="p">(</span><span class="n">metaclass</span><span class="o">=</span><span class="n">PersonMeta</span><span class="p">):</span>
    <span class="sd">"""Person interface built from PersonMeta metaclass."""</span>
    <span class="k">pass</span>
</code></pre></div>
<p>Here, you have the setup for creating your virtual base classes:</p>
<ol>
<li>The metaclass <code>PersonMeta</code></li>
<li>The base class <code>PersonSuper</code></li>
<li>The Python interface <code>Person</code></li>
</ol>
<p>Now that the setup for creating <strong>virtual base classes</strong> is done you’ll define two concrete classes, <code>Employee</code> and <code>Friend</code>. The <code>Employee</code> class inherits from <code>PersonSuper</code>, while <code>Friend</code> implicitly inherits from <code>Person</code>:</p>
<div class="highlight python"><pre><span></span><code><span class="c1"># Inheriting subclasses</span>
<span class="k">class</span> <span class="nc">Employee</span><span class="p">(</span><span class="n">PersonSuper</span><span class="p">):</span>
    <span class="sd">"""Inherits from PersonSuper</span>
<span class="sd">    PersonSuper will appear in Employee.__mro__</span>
<span class="sd">    """</span>
    <span class="k">pass</span>

<span class="k">class</span> <span class="nc">Friend</span><span class="p">:</span>
    <span class="sd">"""Built implicitly from Person</span>
<span class="sd">    Friend is a virtual subclass of Person since</span>
<span class="sd">    both required methods exist.</span>
<span class="sd">    Person not in Friend.__mro__</span>
<span class="sd">    """</span>
    <span class="k">def</span> <span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">age</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>
</code></pre></div>
<p>Although <code>Friend</code> does not explicitly inherit from <code>Person</code>, it implements <code>.name()</code> and <code>.age()</code>, so <code>Person</code> becomes a <strong>virtual base class</strong> of <code>Friend</code>. When you run <code>issubclass(Friend, Person)</code> it should return <code>True</code>, meaning that <code>Friend</code> is a subclass of <code>Person</code>.</p>
<p>The following <a href="https://realpython.com/inheritance-composition-python/#whats-inheritance"><strong>UML</strong></a> diagram shows what happens when you call <code>issubclass()</code> on the <code>Friend</code> class:</p>
<p><a href="./Request_files/virtual-base-class.webp" target="_blank"><img loading="lazy" class="img-fluid mx-auto d-block " src="./Request_files/virtual-base-class.webp" width="401" height="241" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/virtual-base-class.b545144aafef.png&amp;w=100&amp;sig=11a2043e7a54364bcf7f2e8789f61a5a842a5f93 100w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/virtual-base-class.b545144aafef.png&amp;w=200&amp;sig=09c75593e5f83b49a6b41ae65465b333c27d73e5 200w, https://files.realpython.com/media/virtual-base-class.b545144aafef.png 401w" sizes="75vw" alt="virtual base class"></a></p>
<p>Taking a look at <code>PersonMeta</code>, you’ll notice that there’s another dunder method called <code>.__instancecheck__()</code>. This method is used to check if instances of <code>Friend</code> are created from the <code>Person</code> interface. Your code will call <code>.__instancecheck__()</code> when you use <code>isinstance(Friend, Person)</code>.</p>
<div class="w-100 text-center js-needs-scaling" style="transform-origin: 0 0;"><div id="waldo-tag-5000" data-processed="true"></div> <a class="small text-muted js-disclosure" href="https://realpython.com/account/join/" rel="nofollow" style="display: none;"> <i aria-hidden="true" class="fa fa-info-circle"> </i> Remove ads</a></div><h2 id="formal-interfaces">Formal Interfaces</h2>
<p>Informal interfaces can be useful for projects with a small code base and a limited number of programmers. However, informal interfaces would be the wrong approach for larger applications. In order to create a <strong>formal Python interface</strong>, you’ll need a few more tools from Python’s <code>abc</code> module.</p>
<h3 id="using-abcabcmeta">Using <code>abc.ABCMeta</code></h3>
<p>To enforce the subclass instantiation of abstract methods, you’ll utilize Python’s builtin <code>ABCMeta</code> from the <a href="https://docs.python.org/3/library/abc.html"><code>abc</code></a> module. Going back to your <code>UpdatedInformalParserInterface</code> interface, you created your own metaclass, <code>ParserMeta</code>, with the overridden dunder methods <code>.__instancecheck__()</code> and <code>.__subclasscheck__()</code>.</p>
<p>Rather than create your own metaclass, you’ll use <code>abc.ABCMeta</code> as the metaclass. Then, you’ll overwrite <code>.__subclasshook__()</code> in place of <code>.__instancecheck__()</code> and <code>.__subclasscheck__()</code>, as it creates a more reliable implementation of these dunder methods.</p>
<h3 id="using-__subclasshook__">Using <code>.__subclasshook__()</code></h3>
<p>Here’s the implementation of <code>FormalParserInterface</code> using <code>abc.ABCMeta</code> as your metaclass:</p>
<div class="highlight python"><pre><span></span><code><span class="kn">import</span> <span class="nn">abc</span>

<span class="k">class</span> <span class="nc">FormalParserInterface</span><span class="p">(</span><span class="n">metaclass</span><span class="o">=</span><span class="n">abc</span><span class="o">.</span><span class="n">ABCMeta</span><span class="p">):</span>
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">__subclasshook__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">subclass</span><span class="p">):</span>
        <span class="k">return</span> <span class="p">(</span><span class="nb">hasattr</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="s1">'load_data_source'</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="n">callable</span><span class="p">(</span><span class="n">subclass</span><span class="o">.</span><span class="n">load_data_source</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="nb">hasattr</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="s1">'extract_text'</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="n">callable</span><span class="p">(</span><span class="n">subclass</span><span class="o">.</span><span class="n">extract_text</span><span class="p">))</span>

<span class="k">class</span> <span class="nc">PdfParserNew</span><span class="p">:</span>
    <span class="sd">"""Extract text from a PDF."""</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Overrides FormalParserInterface.load_data_source()"""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""Overrides FormalParserInterface.extract_text()"""</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">EmlParserNew</span><span class="p">:</span>
    <span class="sd">"""Extract text from an email."""</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Overrides FormalParserInterface.load_data_source()"""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text_from_email</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""A method defined only in EmlParser.</span>
<span class="sd">        Does not override FormalParserInterface.extract_text()</span>
<span class="sd">        """</span>
        <span class="k">pass</span>
</code></pre></div>
<p>If you run <code>issubclass()</code> on <code>PdfParserNew</code> and <code>EmlParserNew</code>, then <code>issubclass()</code> will return <code>True</code> and <code>False</code>, respectively. </p>
<h3 id="using-abc-to-register-a-virtual-subclass">Using <code>abc</code> to Register a Virtual Subclass</h3>
<p>Once you’ve imported the <code>abc</code> module, you can directly <strong>register a virtual subclass</strong> by using the <code>.register()</code> metamethod. In the next example, you register the interface <code>Double</code> as a virtual base class of the built-in <code>__float__</code> class:</p>
<div class="highlight python"><pre><span></span><code><span class="k">class</span> <span class="nc">Double</span><span class="p">(</span><span class="n">metaclass</span><span class="o">=</span><span class="n">abc</span><span class="o">.</span><span class="n">ABCMeta</span><span class="p">):</span>
    <span class="sd">"""Double precision floating point number."""</span>
    <span class="k">pass</span>

<span class="n">Double</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="nb">float</span><span class="p">)</span>
</code></pre></div>
<p>You can check out the effect of using <code>.register()</code>:</p>
<div class="highlight python repl"><span class="repl-toggle" title="Toggle REPL prompts and output">&gt;&gt;&gt;</span><pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="nb">issubclass</span><span class="p">(</span><span class="nb">float</span><span class="p">,</span> <span class="n">Double</span><span class="p">)</span>
<span class="go">True</span>

<span class="gp">&gt;&gt;&gt; </span><span class="nb">isinstance</span><span class="p">(</span><span class="mf">1.2345</span><span class="p">,</span> <span class="n">Double</span><span class="p">)</span>
<span class="go">True</span>
</code></pre></div>
<p>By using the <code>.register()</code> meta method, you’ve successfully registered <code>Double</code> as a virtual subclass of <code>float</code>.</p>
<p>Once you’ve registered <code>Double</code>, you can use it as class <a href="https://realpython.com/courses/python-decorators-101/">decorator</a> to set the decorated class as a virtual subclass:</p>
<div class="highlight python"><pre><span></span><code><span class="nd">@Double</span><span class="o">.</span><span class="n">register</span>
<span class="k">class</span> <span class="nc">Double64</span><span class="p">:</span>
    <span class="sd">"""A 64-bit double-precision floating-point number."""</span>
    <span class="k">pass</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">issubclass</span><span class="p">(</span><span class="n">Double64</span><span class="p">,</span> <span class="n">Double</span><span class="p">))</span>  <span class="c1"># True</span>
</code></pre></div>
<p>The decorator register method helps you to create a hierarchy of custom virtual class inheritance.</p>
<h3 id="using-subclass-detection-with-registration">Using Subclass Detection With Registration</h3>
<p>You must be careful when you’re combining <code>.__subclasshook__()</code> with <code>.register()</code>, as <code>.__subclasshook__()</code> takes precedence over virtual subclass registration. To ensure that the registered virtual subclasses are taken into consideration, you must add <code>NotImplemented</code> to the <code>.__subclasshook__()</code> dunder method. The <code>FormalParserInterface</code> would be updated to the following:</p>
<div class="highlight python"><pre><span></span><code><span class="k">class</span> <span class="nc">FormalParserInterface</span><span class="p">(</span><span class="n">metaclass</span><span class="o">=</span><span class="n">abc</span><span class="o">.</span><span class="n">ABCMeta</span><span class="p">):</span>
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">__subclasshook__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">subclass</span><span class="p">):</span>
        <span class="k">return</span> <span class="p">(</span><span class="nb">hasattr</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="s1">'load_data_source'</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="n">callable</span><span class="p">(</span><span class="n">subclass</span><span class="o">.</span><span class="n">load_data_source</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="nb">hasattr</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="s1">'extract_text'</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="n">callable</span><span class="p">(</span><span class="n">subclass</span><span class="o">.</span><span class="n">extract_text</span><span class="p">)</span> <span class="ow">or</span> 
                <span class="bp">NotImplemented</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">PdfParserNew</span><span class="p">:</span>
    <span class="sd">"""Extract text from a PDF."""</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Overrides FormalParserInterface.load_data_source()"""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""Overrides FormalParserInterface.extract_text()"""</span>
        <span class="k">pass</span>

<span class="nd">@FormalParserInterface</span><span class="o">.</span><span class="n">register</span>
<span class="k">class</span> <span class="nc">EmlParserNew</span><span class="p">:</span>
    <span class="sd">"""Extract text from an email."""</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Overrides FormalParserInterface.load_data_source()"""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text_from_email</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""A method defined only in EmlParser.</span>
<span class="sd">        Does not override FormalParserInterface.extract_text()</span>
<span class="sd">        """</span>
        <span class="k">pass</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">issubclass</span><span class="p">(</span><span class="n">PdfParserNew</span><span class="p">,</span> <span class="n">FormalParserInterface</span><span class="p">))</span>  <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">issubclass</span><span class="p">(</span><span class="n">EmlParserNew</span><span class="p">,</span> <span class="n">FormalParserInterface</span><span class="p">))</span>  <span class="c1"># True</span>
</code></pre></div>
<p>Since you’ve used registration, you can see that <code>EmlParserNew</code> is considered a virtual subclass of your <code>FormalParserInterface</code> interface. This is not what you wanted since <code>EmlParserNew</code> doesn’t override <code>.extract_text()</code>. <strong>Please use caution with virtual subclass registration!</strong></p>
<div class="w-100 text-center js-needs-scaling" style="transform-origin: 0 0;"><div id="waldo-tag-5002" data-processed="true"></div> <a class="small text-muted js-disclosure" href="https://realpython.com/account/join/" rel="nofollow" style="display: none;"> <i aria-hidden="true" class="fa fa-info-circle"> </i> Remove ads</a></div><h3 id="using-abstract-method-declaration">Using Abstract Method Declaration</h3>
<p>An <strong>abstract method</strong> is a method that’s declared by the Python interface, but it may not have a useful implementation. The abstract method must be overridden by the concrete class that implements the interface in question.</p>
<p>To create abstract methods in Python, you add the <code>@abc.abstractmethod</code> decorator to the interface’s methods. In the next example, you update the <code>FormalParserInterface</code> to include the abstract methods <code>.load_data_source()</code> and <code>.extract_text()</code>:</p>
<div class="highlight python"><pre><span></span><code><span class="k">class</span> <span class="nc">FormalParserInterface</span><span class="p">(</span><span class="n">metaclass</span><span class="o">=</span><span class="n">abc</span><span class="o">.</span><span class="n">ABCMeta</span><span class="p">):</span>
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">__subclasshook__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">subclass</span><span class="p">):</span>
        <span class="k">return</span> <span class="p">(</span><span class="nb">hasattr</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="s1">'load_data_source'</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="n">callable</span><span class="p">(</span><span class="n">subclass</span><span class="o">.</span><span class="n">load_data_source</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="nb">hasattr</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="s1">'extract_text'</span><span class="p">)</span> <span class="ow">and</span> 
                <span class="n">callable</span><span class="p">(</span><span class="n">subclass</span><span class="o">.</span><span class="n">extract_text</span><span class="p">)</span> <span class="ow">or</span> 
                <span class="bp">NotImplemented</span><span class="p">)</span>

    <span class="nd">@abc</span><span class="o">.</span><span class="n">abstractmethod</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="sd">"""Load in the data set"""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

    <span class="nd">@abc</span><span class="o">.</span><span class="n">abstractmethod</span>
    <span class="k">def</span> <span class="nf">extract_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="sd">"""Extract text from the data set"""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

<span class="k">class</span> <span class="nc">PdfParserNew</span><span class="p">(</span><span class="n">FormalParserInterface</span><span class="p">):</span>
    <span class="sd">"""Extract text from a PDF."""</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Overrides FormalParserInterface.load_data_source()"""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""Overrides FormalParserInterface.extract_text()"""</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">EmlParserNew</span><span class="p">(</span><span class="n">FormalParserInterface</span><span class="p">):</span>
    <span class="sd">"""Extract text from an email."""</span>
    <span class="k">def</span> <span class="nf">load_data_source</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="sd">"""Overrides FormalParserInterface.load_data_source()"""</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">extract_text_from_email</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="sd">"""A method defined only in EmlParser.</span>
<span class="sd">        Does not override FormalParserInterface.extract_text()</span>
<span class="sd">        """</span>
        <span class="k">pass</span>
</code></pre></div>
<p>In the above example, you’ve finally created a formal interface that will raise errors when the abstract methods aren’t overridden. The <code>PdfParserNew</code> instance, <code>pdf_parser</code>, won’t raise any errors, as <code>PdfParserNew</code> is correctly overriding the <code>FormalParserInterface</code> abstract methods. However, <code>EmlParserNew</code> will raise an error:</p>
<div class="highlight python repl"><span class="repl-toggle" title="Toggle REPL prompts and output">&gt;&gt;&gt;</span><pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">pdf_parser</span> <span class="o">=</span> <span class="n">PdfParserNew</span><span class="p">()</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">eml_parser</span> <span class="o">=</span> <span class="n">EmlParserNew</span><span class="p">()</span>
<span class="gt">Traceback (most recent call last):</span>
  File <span class="nb">"real_python_interfaces.py"</span>, line <span class="m">53</span>, in <span class="n">&lt;module&gt;</span>
    <span class="n">eml_interface</span> <span class="o">=</span> <span class="n">EmlParserNew</span><span class="p">()</span>
<span class="gr">TypeError</span>: <span class="n">Can't instantiate abstract class EmlParserNew with abstract methods extract_text</span>
</code></pre></div>
<p>As you can see, the <a href="https://realpython.com/python-traceback/">traceback</a> message tells you that you haven’t overridden all the abstract methods. This is the behavior you expect when building a formal Python interface.</p>
<h2 id="interfaces-in-other-languages">Interfaces in Other Languages</h2>
<p>Interfaces appear in many programming languages, and their implementation varies greatly from language to language. In the next few sections, you’ll compare interfaces in Python to Java, C++, and Go.</p>
<h3 id="java">Java</h3>
<p>Unlike Python, <a href="https://realpython.com/oop-in-python-vs-java/">Java</a> contains an <code>interface</code> keyword. Keeping with the file parser example, you declare an interface in Java like so:</p>
<div class="highlight java"><pre><span></span><code><span class="kd">public</span> <span class="kd">interface</span> <span class="nc">FileParserInterface</span> <span class="p">{</span>
    <span class="c1">// Static fields, and abstract methods go here ...</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">loadDataSource</span><span class="p">();</span>
    <span class="kd">public</span> <span class="kt">void</span> <span class="nf">extractText</span><span class="p">();</span>
<span class="p">}</span>
</code></pre></div>
<p>Now you’ll create two concrete classes, <code>PdfParser</code> and <code>EmlParser</code>, to implement the <code>FileParserInterface</code>. To do so, you must use the <code>implements</code> keyword in the class definition, like so:</p>
<div class="highlight java"><pre><span></span><code><span class="kd">public</span> <span class="kd">class</span> <span class="nc">EmlParser</span> <span class="kd">implements</span> <span class="n">FileParserInterface</span> <span class="p">{</span>
     <span class="kd">public</span> <span class="kt">void</span> <span class="nf">loadDataSource</span><span class="p">()</span> <span class="p">{</span>
            <span class="c1">// Code to load the data set</span>
        <span class="p">}</span>

     <span class="kd">public</span> <span class="kt">void</span> <span class="nf">extractText</span><span class="p">()</span> <span class="p">{</span>
            <span class="c1">// Code to extract the text</span>
        <span class="p">}</span>
<span class="p">}</span>
</code></pre></div>
<p>Continuing with your file parsing example, a fully-functional Java interface would look something like this:</p>
<div class="highlight java"><pre><span></span><code><span class="kn">import</span> <span class="nn">java.util.*</span><span class="p">;</span>
<span class="kn">import</span> <span class="nn">java.io.*</span><span class="p">;</span>

<span class="kd">public</span> <span class="kd">class</span> <span class="nc">FileParser</span> <span class="p">{</span>
    <span class="kd">public</span> <span class="kd">static</span> <span class="kt">void</span> <span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span> <span class="n">args</span><span class="p">)</span> <span class="kd">throws</span> <span class="n">IOException</span> <span class="p">{</span>
        <span class="c1">// The main entry point</span>
    <span class="p">}</span>

    <span class="kd">public</span> <span class="kd">interface</span> <span class="nc">FileParserInterface</span> <span class="p">{</span>
        <span class="n">HashMap</span><span class="o">&lt;</span><span class="n">String</span><span class="p">,</span> <span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;&gt;</span> <span class="n">file_contents</span> <span class="o">=</span> <span class="kc">null</span><span class="p">;</span>

        <span class="kd">public</span> <span class="kt">void</span> <span class="nf">loadDataSource</span><span class="p">();</span>
        <span class="kd">public</span> <span class="kt">void</span> <span class="nf">extractText</span><span class="p">();</span>
    <span class="p">}</span>

    <span class="kd">public</span> <span class="kd">class</span> <span class="nc">PdfParser</span> <span class="kd">implements</span> <span class="n">FileParserInterface</span> <span class="p">{</span>
        <span class="kd">public</span> <span class="kt">void</span> <span class="nf">loadDataSource</span><span class="p">()</span> <span class="p">{</span>
            <span class="c1">// Code to load the data set</span>
        <span class="p">}</span>

        <span class="kd">public</span> <span class="kt">void</span> <span class="nf">extractText</span><span class="p">()</span> <span class="p">{</span>
            <span class="c1">// Code to extract the text</span>
        <span class="p">}</span>

    <span class="p">}</span>

    <span class="kd">public</span> <span class="kd">class</span> <span class="nc">EmlParser</span> <span class="kd">implements</span> <span class="n">FileParserInterface</span> <span class="p">{</span>
        <span class="kd">public</span> <span class="kt">void</span> <span class="nf">loadDataSource</span><span class="p">()</span> <span class="p">{</span>
            <span class="c1">// Code to load the data set</span>
        <span class="p">}</span>

        <span class="kd">public</span> <span class="kt">void</span> <span class="nf">extractText</span><span class="p">()</span> <span class="p">{</span>
            <span class="c1">// Code to extract the text</span>
        <span class="p">}</span>
    <span class="p">}</span>

<span class="p">}</span>
</code></pre></div>
<p>As you can see, a Python interface gives you much more flexibility during creation than a Java interface does.</p>
<h3 id="c">C++</h3>
<p>Like Python, C++ uses abstract base classes to create interfaces. When defining an interface in C++, you use the keyword <code>virtual</code> to describe a method that should be overwritten in the concrete class:</p>
<div class="highlight cpp"><pre><span></span><code><span class="k">class</span> <span class="nc">FileParserInterface</span> <span class="p">{</span>

    <span class="k">public</span><span class="o">:</span>
        <span class="k">virtual</span> <span class="kt">void</span> <span class="n">loadDataSource</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">path</span><span class="p">,</span> <span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">file_name</span><span class="p">);</span>
        <span class="k">virtual</span> <span class="kt">void</span> <span class="nf">extractText</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">full_file_name</span><span class="p">);</span>
<span class="p">};</span>
</code></pre></div>
<p>When you want to implement the interface, you’ll give the concrete class name, followed by a colon (<code>:</code>), and then the name of the interface. The following example demonstrates C++ interface implementation:</p>
<div class="highlight cpp"><pre><span></span><code><span class="k">class</span> <span class="nc">PdfParser</span> <span class="o">:</span> <span class="n">FileParserInterface</span> <span class="p">{</span>
    <span class="k">public</span><span class="o">:</span>
        <span class="kt">void</span> <span class="n">loadDataSource</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">path</span><span class="p">,</span> <span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">file_name</span><span class="p">);</span>
        <span class="kt">void</span> <span class="nf">extractText</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">full_file_name</span><span class="p">);</span>
<span class="p">};</span>

<span class="k">class</span> <span class="nc">EmlParser</span> <span class="o">:</span> <span class="n">FileParserInterface</span> <span class="p">{</span>
    <span class="k">public</span><span class="o">:</span>
        <span class="kt">void</span> <span class="n">loadDataSource</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">path</span><span class="p">,</span> <span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">file_name</span><span class="p">);</span>
        <span class="kt">void</span> <span class="nf">extractText</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">full_file_name</span><span class="p">);</span>
<span class="p">};</span>
</code></pre></div>
<p>A Python interface and a C++ interface have some similarities in that they both make use of abstract base classes to simulate interfaces.</p>
<div class="w-100 text-center js-needs-scaling" style="transform-origin: 0 0;"><div id="waldo-tag-5004" data-processed="true"></div> <a class="small text-muted js-disclosure" href="https://realpython.com/account/join/" rel="nofollow" style="display: none;"> <i aria-hidden="true" class="fa fa-info-circle"> </i> Remove ads</a></div><h3 id="go">Go</h3>
<p>Although Go’s syntax is reminiscent of Python, the Go programming language contains an <code>interface</code> keyword, like Java. Let’s create the <code>fileParserInterface</code> in Go:</p>
<div class="highlight go"><pre><span></span><code><span class="kd">type</span> <span class="nx">fileParserInterface</span> <span class="kd">interface</span> <span class="p">{</span>
        <span class="nx">loadDataSet</span><span class="p">(</span><span class="nx">path</span> <span class="kt">string</span><span class="p">,</span> <span class="nx">filename</span> <span class="kt">string</span><span class="p">)</span>
        <span class="nx">extractText</span><span class="p">(</span><span class="nx">full_file_path</span> <span class="kt">string</span><span class="p">)</span>
<span class="p">}</span>
</code></pre></div>
<p>A big difference between Python and Go is that Go doesn’t have classes. Rather, Go is similar to <a href="https://realpython.com/build-python-c-extension-module/">C</a> in that it uses the <code>struct</code> keyword to create structures. A <strong>structure</strong> is similar to a class in that a structure contains data and methods. However, unlike a class, all of the data and methods are publicly accessed. The concrete structs in Go will be used to implement the <code>fileParserInterface</code>.</p>
<p>Here’s an example of how Go uses interfaces:</p>
<div class="highlight go"><pre><span></span><code><span class="kn">package</span> <span class="nx">main</span>

<span class="kd">type</span> <span class="nx">fileParserInterface</span> <span class="kd">interface</span> <span class="p">{</span>
        <span class="nx">loadDataSet</span><span class="p">(</span><span class="nx">path</span> <span class="kt">string</span><span class="p">,</span> <span class="nx">filename</span> <span class="kt">string</span><span class="p">)</span>
        <span class="nx">extractText</span><span class="p">(</span><span class="nx">full_file_path</span> <span class="kt">string</span><span class="p">)</span>
<span class="p">}</span>

<span class="kd">type</span> <span class="nx">pdfParser</span> <span class="kd">struct</span> <span class="p">{</span>
        <span class="c1">// Data goes here ...</span>
<span class="p">}</span>

<span class="kd">type</span> <span class="nx">emlParser</span> <span class="kd">struct</span> <span class="p">{</span>
        <span class="c1">// Data goes here ...</span>
<span class="p">}</span>

<span class="kd">func</span> <span class="p">(</span><span class="nx">p</span> <span class="nx">pdfParser</span><span class="p">)</span> <span class="nx">loadDataSet</span><span class="p">()</span> <span class="p">{</span>
        <span class="c1">// Method definition ...</span>
<span class="p">}</span>

<span class="kd">func</span> <span class="p">(</span><span class="nx">p</span> <span class="nx">pdfParser</span><span class="p">)</span> <span class="nx">extractText</span><span class="p">()</span> <span class="p">{</span>
        <span class="c1">// Method definition ...</span>
<span class="p">}</span>

<span class="kd">func</span> <span class="p">(</span><span class="nx">e</span> <span class="nx">emlParser</span><span class="p">)</span> <span class="nx">loadDataSet</span><span class="p">()</span> <span class="p">{</span>
        <span class="c1">// Method definition ...</span>
<span class="p">}</span>

<span class="kd">func</span> <span class="p">(</span><span class="nx">e</span> <span class="nx">emlParser</span><span class="p">)</span> <span class="nx">extractText</span><span class="p">()</span> <span class="p">{</span>
        <span class="c1">// Method definition ...</span>
<span class="p">}</span>

<span class="kd">func</span> <span class="nx">main</span><span class="p">()</span> <span class="p">{</span>
        <span class="c1">// Main entrypoint</span>
<span class="p">}</span>
</code></pre></div>
<p>Unlike a Python interface, a Go interface is created using structs and the explicit keyword <code>interface</code>.</p>
<h2 id="conclusion">Conclusion</h2>
<p>Python offers great flexibility when you’re creating interfaces. An informal Python interface is useful for small projects where you’re less likely to get confused as to what the return types of the methods are. As a project grows, the need for a <strong>formal Python interface</strong> becomes more important as it becomes more difficult to infer return types. This ensures that the concrete class, which implements the interface, overwrites the abstract methods.</p>
<p><strong>Now you can:</strong></p>
<ul>
<li>Understand <strong>how interfaces work</strong> and the caveats of creating a Python interface</li>
<li>Understand the <strong>usefulness</strong> of interfaces in a dynamic language like Python</li>
<li>Implement <strong>formal and informal</strong> interfaces in Python</li>
<li><strong>Compare Python interfaces</strong> to those in languages like Java, C++, and Go</li>
</ul>
<p>Now that you’ve become familiar with how to create a Python interface, add a Python interface to your next project to see its usefulness in action!</p>
</div>
<div class="card mt-4 mb-4 bg-secondary">
<p class="card-header h3 text-center bg-light">🐍 Python Tricks 💌</p>
<div class="card-body">
<div class="container">
<div class="row">
<div class="col-xs-12 col-sm-7">
<p>Get a short &amp; sweet <strong>Python Trick</strong> delivered to your inbox every couple of days. No spam ever. Unsubscribe any time. Curated by the Real Python team.</p>
</div>
<div class="col-xs-12 col-sm-5">
<img class="img-fluid rounded mb-3" src="./Request_files/pytrick-dict-merge.webp" width="738" height="490" alt="Python Tricks Dictionary Merge">
</div>
</div>
<div class="row mb-3">
<form class="col-12" action="https://realpython.com/optins/process/" method="post">
<input type="hidden" name="csrfmiddlewaretoken" value="ot8OKZL0ue2HgloPnd6ooKWJydPOUqQG4SGH3KGjsc7SOTOSruNNJO3N5KmF76zo">
<input type="hidden" name="slug" value="static-python-tricks-footer">
<div class="form-group">
<input name="email" type="email" class="form-control form-control-lg" placeholder="Email Address" required="">
</div>
<button name="submit" type="submit" class="btn btn-primary btn-lg btn-block">Send Me Python Tricks »</button>
</form>
</div>
</div>
</div>
</div>
<div class="card mt-3" id="author">
<p class="card-header h3">About <strong>William Murphy</strong></p>
<div class="card-body">
<div class="container p-0">
<div class="row">
<div class="col-12 col-md-3 align-self-center">
<a href="https://realpython.com/team/wmurphy/"><img loading="lazy" src="./Request_files/real-python-logo-square.28474fda9228.png" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/real-python-logo-square.28474fda9228.png&amp;w=375&amp;sig=63b1902b1a7aab334cdf77c17b087777c93eed72 375w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/real-python-logo-square.28474fda9228.png&amp;w=750&amp;sig=43098782d487dd64229435da04c792c4255a9f50 750w, https://files.realpython.com/media/real-python-logo-square.28474fda9228.png 1500w" sizes="25vw" class="d-block d-md-none rounded-circle img-fluid w-33 mb-0 mx-auto" alt="William Murphy"></a>
<a href="https://realpython.com/team/wmurphy/"><img loading="lazy" src="./Request_files/real-python-logo-square.28474fda9228.png" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/real-python-logo-square.28474fda9228.png&amp;w=375&amp;sig=63b1902b1a7aab334cdf77c17b087777c93eed72 375w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/real-python-logo-square.28474fda9228.png&amp;w=750&amp;sig=43098782d487dd64229435da04c792c4255a9f50 750w, https://files.realpython.com/media/real-python-logo-square.28474fda9228.png 1500w" sizes="25vw" class="d-none d-md-block rounded-circle img-fluid w-100 mb-0" alt="William Murphy"></a>
</div>
<div class="col mt-3">
<p>William has been working with Python for over 6 years, working in roles such as data scientist, machine learning engineer, data engineer, and dev ops engineer. He is currently a senior software engineering consultant at ModernDay Productions.</p>
<a href="https://realpython.com/team/wmurphy/" class="card-link">» More about William</a>
</div>
</div>
</div>
</div>
<hr class="my-0">
<div class="card-body pb-0">
<div class="container">
<div class="row">
<p><em>Each tutorial at Real Python is created by a team of developers so that it meets our high quality standards. The team members who worked on this tutorial are:</em></p>
</div>
<div class="row align-items-center w-100 mx-auto">
<div class="col-4 col-sm-2 align-self-center">
<a href="https://realpython.com/team/asantos/"><img loading="lazy" src="./Request_files/asantos-avatar.888c78fffab3.jpg" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/asantos-avatar.888c78fffab3.jpg&amp;w=175&amp;sig=a095ca193d3f40e73e6921403c1c43e48c9a4bdc 175w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/asantos-avatar.888c78fffab3.jpg&amp;w=350&amp;sig=28c0dc29376daf4ca29d5f47b3708b873c21af76 350w, https://files.realpython.com/media/asantos-avatar.888c78fffab3.jpg 700w" sizes="10vw" class="rounded-circle img-fluid w-100" alt="Aldren Santos"></a>
</div>
<div class="col pl-0 d-none d-sm-block">
<a href="https://realpython.com/team/asantos/" class="card-link"><p>Aldren</p></a>
</div>
<div class="col-4 col-sm-2 align-self-center">
<a href="https://realpython.com/team/gahjelle/"><img loading="lazy" src="./Request_files/gahjelle.470149ee709e.jpg" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/gahjelle.470149ee709e.jpg&amp;w=200&amp;sig=5f5c996c1ae71bd7f2f89f547a334d508de2f4bb 200w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/gahjelle.470149ee709e.jpg&amp;w=400&amp;sig=0e74ccf912d97528bda85e7b9e9e5064d69a1169 400w, https://files.realpython.com/media/gahjelle.470149ee709e.jpg 800w" sizes="10vw" class="rounded-circle img-fluid w-100" alt="Geir Arne Hjelle"></a>
</div>
<div class="col pl-0 d-none d-sm-block">
<a href="https://realpython.com/team/gahjelle/" class="card-link"><p>Geir Arne</p></a>
</div>
<div class="col-4 col-sm-2 align-self-center">
<a href="https://realpython.com/team/jayazhane/"><img loading="lazy" src="./Request_files/author-jpowell.ecce5da51b65.jpg" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/author-jpowell.ecce5da51b65.jpg&amp;w=143&amp;sig=b95bfe83fd10d5bf43b3623122ff842fd8dd7574 143w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/author-jpowell.ecce5da51b65.jpg&amp;w=286&amp;sig=ac2be4e646abc20329b882f6389b5e570965609f 286w, https://files.realpython.com/media/author-jpowell.ecce5da51b65.jpg 572w" sizes="10vw" class="rounded-circle img-fluid w-100" alt="Jaya Zhané"></a>
</div>
<div class="col pl-0 d-none d-sm-block">
<a href="https://realpython.com/team/jayazhane/" class="card-link"><p>Jaya</p></a>
 </div>
</div>
<div class="row align-items-center w-100 mx-auto">
<div class="col-4 col-sm-2 align-self-center">
<a href="https://realpython.com/team/jjablonski/"><img loading="lazy" src="./Request_files/jjablonksi-avatar.e37c4f83308e.jpg" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/jjablonksi-avatar.e37c4f83308e.jpg&amp;w=200&amp;sig=d779dbceba743afb659648000525a6a71656ae98 200w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/jjablonksi-avatar.e37c4f83308e.jpg&amp;w=400&amp;sig=99ce401a9a219f6b406309e90925252be1900dfc 400w, https://files.realpython.com/media/jjablonksi-avatar.e37c4f83308e.jpg 800w" sizes="10vw" class="rounded-circle img-fluid w-100" alt="Joanna Jablonski"></a>
</div>
<div class="col pl-0 d-none d-sm-block">
<a href="https://realpython.com/team/jjablonski/" class="card-link"><p>Joanna</p></a>
</div>
<div class="col-4 col-sm-2 align-self-center">
<a href="https://realpython.com/team/mdriscoll/"><img loading="lazy" src="./Request_files/real-python-logo-square.28474fda9228.png" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/real-python-logo-square.28474fda9228.png&amp;w=375&amp;sig=63b1902b1a7aab334cdf77c17b087777c93eed72 375w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/real-python-logo-square.28474fda9228.png&amp;w=750&amp;sig=43098782d487dd64229435da04c792c4255a9f50 750w, https://files.realpython.com/media/real-python-logo-square.28474fda9228.png 1500w" sizes="10vw" class="rounded-circle img-fluid w-100" alt="Mike Driscoll"></a>
</div>
<div class="col pl-0 d-none d-sm-block">
<a href="https://realpython.com/team/mdriscoll/" class="card-link"><p>Mike</p></a>
</div>
<div class="col-4 col-sm-2 align-self-center"></div>
<div class="col pl-0 d-none d-sm-block"></div>
</div>
</div>
</div>
</div>
<div class="bg-light rounded py-4 my-4 shadow shadow-sm mx-n2">
<div class="col-12 text-center d-block d-md-none">
<p class="h2 mb-3">Master <u><span class="marker-highlight">Real-World Python Skills</span></u> With Unlimited Access to Real&nbsp;Python</p>
<p class="mb-1"><img class="w-75" src="./Request_files/lesson-locked.f5105cfd26db.svg"></p>
<p class="mx-auto w-75 mb-3 small"><strong>Join us and get access to hundreds of tutorials, hands-on video courses, and a community of expert&nbsp;Pythonistas:</strong></p>
<p class="mb-0"><a href="https://realpython.com/account/join/?utm_source=rp_article_footer&amp;utm_content=python-interface" class="btn btn-primary btn-sm px-4 mb-0">Level Up Your Python Skills »</a>
</p></div>
<div class="col-12 text-center d-none d-md-block">
<p class="h2 mb-2">Master <u><span class="marker-highlight">Real-World Python Skills</span></u><br>With Unlimited Access to Real&nbsp;Python</p>
<p class="mb-2"><img class="w-50 mb-2" src="./Request_files/lesson-locked.f5105cfd26db.svg"></p>
<p class="mx-auto w-50 mb-3"><strong>Join us and get access to hundreds of tutorials, hands-on video courses, and a community of expert Pythonistas:</strong></p>
<p><a href="https://realpython.com/account/join/?utm_source=rp_article_footer&amp;utm_content=python-interface" class="btn btn-primary btn-lg px-4">Level Up Your Python Skills »</a>
</p></div>
</div>
<div class="card mt-4" id="reader-comments">
<p class="card-header h3">What Do You Think?</p>
<div class="text-center mt-3 mb-0 p-0">
<span>
<a target="_blank" rel="nofollow" href="https://twitter.com/intent/tweet/?text=Check%20out%20this%20%23Python%20tutorial:%20Implementing%20an%20Interface%20in%20Python%20by%20@realpython&amp;url=https%3A//realpython.com/python-interface/" class="mr-1 badge badge-twitter text-light mb-1"><i class="mr-1 fa fa-twitter text-light"></i>Tweet</a>
<a target="_blank" rel="nofollow" href="https://facebook.com/sharer/sharer.php?u=https%3A//realpython.com/python-interface/" class="mr-1 badge badge-facebook text-light mb-1"><i class="mr-1 fa fa-facebook text-light"></i>Share</a>
<a target="_blank" rel="nofollow" href="mailto:?subject=Python%20article%20for%20you&amp;body=Check%20out%20this%20Python%20tutorial:%0A%0AImplementing%20an%20Interface%20in%20Python%0A%0Ahttps%3A//realpython.com/python-interface/" class="mr-1 badge badge-red text-light mb-1"><i class="mr-1 fa fa-envelope text-light"></i>Email</a>
</span>
</div>
<div class="card-body">
<div class="alert alert-dark">
<p class="mb-0"><strong>Real Python Comment Policy:</strong> The most useful comments are those written with the goal of learning from or helping out other readers—after reading the whole article and all the earlier comments. Complaints and insults generally won’t make the cut here.</p>
</div>
<p>What’s your #1 takeaway or favorite thing you learned? How are you going to put your newfound skills to use? Leave a comment below and let us know.</p>
<div class="mb-4" id="disqus_thread">
</div>
</div>
</div>
<div class="card mt-4 mb-4">
<p class="card-header h3">Keep Learning</p>
<div class="card-body">
<p class="mb-0">Related Tutorial Categories:
<a href="https://realpython.com/tutorials/advanced/" class="badge badge-light text-muted">advanced</a>
<a href="https://realpython.com/tutorials/python/" class="badge badge-light text-muted">python</a>
</p>
</div>
</div>
<div class="modal fade" tabindex="-1" role="dialog" id="rpvc">
<div class="modal-dialog modal-lg modal-dialog-centered" role="document">
<div class="modal-content">
<div class="modal-header border-0 mt-3">
<div class="col-12 modal-title text-center">
<h2 class="my-0 mx-5">Master <u>Real-World Python Skills</u> With Unlimited Access to Real Python</h2>
<p class="text-center text-muted mt-2 mb-1">Already a member? <a href="https://realpython.com/account/login/">Sign-In</a></p>
</div>
</div>
<div class="modal-body bg-light">
<div class="col-12 text-center">
<p class="mb-2 mt-3"><a href="https://realpython.com/account/join/?utm_source=rp&amp;utm_medium=web&amp;utm_campaign=pwn&amp;utm_content=v1"><img class="w-50 mb-2" src="./Request_files/lesson-locked.f5105cfd26db.svg"></a></p>
<p class="mx-auto w-66 mb-3"><strong>Join us and get access to hundreds of tutorials, hands-on video courses, and a community of expert Pythonistas:</strong></p>
<p><a href="https://realpython.com/account/join/?utm_source=rp&amp;utm_medium=web&amp;utm_campaign=pwn&amp;utm_content=v1" class="btn btn-primary btn-lg px-4">See Membership Options »</a>
</p></div>
</div>
<div class="modal-footer border-0">
<a href="https://realpython.com/python-interface/#!" class="text-muted btn" data-dismiss="modal">Close</a>
</div>
</div>
</div>
</div>
</div>
<aside class="col-md-7 col-lg-4">
<div class="card mb-3 bg-secondary">
<form class="card-body" action="https://realpython.com/optins/process/" method="post">
<div class="form-group">
<p class="h5 text-muted text-center">— FREE Email Series —</p>
<p class="h3 text-center">🐍 Python Tricks 💌</p>
<p><img class="img-fluid rounded" src="./Request_files/pytrick-dict-merge.webp" width="738" height="490" alt="Python Tricks Dictionary Merge"></p>
</div>
<div class="form-group">
<input type="hidden" name="csrfmiddlewaretoken" value="ot8OKZL0ue2HgloPnd6ooKWJydPOUqQG4SGH3KGjsc7SOTOSruNNJO3N5KmF76zo">
<input type="hidden" name="slug" value="static-python-tricks-sidebar">
<input type="email" class="form-control form-control-md" name="email" placeholder="Email…" required="">
</div>
<button type="submit" name="submit" class="btn btn-primary btn-md btn-block">Get Python Tricks »</button>
<p class="mb-0 mt-2 text-muted text-center">🔒 No spam. Unsubscribe any time.</p>
</form>
</div>
<div class="sidebar-module sidebar-module-inset border">
<p class="h4"><a class="link-unstyled" href="https://realpython.com/tutorials/all/">All Tutorial Topics</a></p>
<a href="https://realpython.com/tutorials/advanced/" class="badge badge-light text-muted">advanced</a>
<a href="https://realpython.com/tutorials/api/" class="badge badge-light text-muted">api</a>
<a href="https://realpython.com/tutorials/basics/" class="badge badge-light text-muted">basics</a>
<a href="https://realpython.com/tutorials/best-practices/" class="badge badge-light text-muted">best-practices</a>
<a href="https://realpython.com/tutorials/community/" class="badge badge-light text-muted">community</a>
<a href="https://realpython.com/tutorials/databases/" class="badge badge-light text-muted">databases</a>
<a href="https://realpython.com/tutorials/data-science/" class="badge badge-light text-muted">data-science</a>
<a href="https://realpython.com/tutorials/devops/" class="badge badge-light text-muted">devops</a>
<a href="https://realpython.com/tutorials/django/" class="badge badge-light text-muted">django</a>
<a href="https://realpython.com/tutorials/docker/" class="badge badge-light text-muted">docker</a>
<a href="https://realpython.com/tutorials/flask/" class="badge badge-light text-muted">flask</a>
<a href="https://realpython.com/tutorials/front-end/" class="badge badge-light text-muted">front-end</a>
<a href="https://realpython.com/tutorials/intermediate/" class="badge badge-light text-muted">intermediate</a>
<a href="https://realpython.com/tutorials/machine-learning/" class="badge badge-light text-muted">machine-learning</a>
<a href="https://realpython.com/tutorials/python/" class="badge badge-light text-muted">python</a>
<a href="https://realpython.com/tutorials/testing/" class="badge badge-light text-muted">testing</a>
<a href="https://realpython.com/tutorials/tools/" class="badge badge-light text-muted">tools</a>
<a href="https://realpython.com/tutorials/web-dev/" class="badge badge-light text-muted">web-dev</a>
<a href="https://realpython.com/tutorials/web-scraping/" class="badge badge-light text-muted">web-scraping</a>
</div>
<div class="sidebar-module sidebar-module-inset p-0" style="overflow:hidden;">
<div style="display:block;position:relative;">
<div style="display:block;width:100%;padding-top:100%;"></div>
<div class="rpad" data-unit="1x1" style="position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;"><a href="https://srv.realpython.net/click/27410864300/?c=50370534298&amp;p=58946116052&amp;r=35789" rel="nofollow" target="_blank"><img src="./Request_files/6c48676ea2154d825ae738d7dd972b6b" style="max-width: 100%; max-height: 100%; width: 100%;"></a></div>
</div>
</div>
<div class="sidebar-sticky">
<div class="sidebar-module sidebar-module-inset border">
<p class="h4"><a class="link-unstyled" href="https://realpython.com/python-interface/#toc">Table of Contents</a></p>
<div class="toc">
<ul>
<li><a href="https://realpython.com/python-interface/#python-interface-overview">Python Interface Overview</a></li>
<li><a href="https://realpython.com/python-interface/#informal-interfaces">Informal Interfaces</a><ul>
<li><a href="https://realpython.com/python-interface/#using-metaclasses">Using Metaclasses</a></li>
<li><a href="https://realpython.com/python-interface/#using-virtual-base-classes">Using Virtual Base Classes</a></li>
</ul>
</li>
<li><a href="https://realpython.com/python-interface/#formal-interfaces">Formal Interfaces</a><ul>
<li><a href="https://realpython.com/python-interface/#using-abcabcmeta">Using abc.ABCMeta</a></li>
<li><a href="https://realpython.com/python-interface/#using-__subclasshook__">Using .__subclasshook__()</a></li>
<li><a href="https://realpython.com/python-interface/#using-abc-to-register-a-virtual-subclass">Using abc to Register a Virtual Subclass</a></li>
<li><a href="https://realpython.com/python-interface/#using-subclass-detection-with-registration">Using Subclass Detection With Registration</a></li>
<li><a href="https://realpython.com/python-interface/#using-abstract-method-declaration">Using Abstract Method Declaration</a></li>
</ul>
</li>
<li><a href="https://realpython.com/python-interface/#interfaces-in-other-languages">Interfaces in Other Languages</a><ul>
<li><a href="https://realpython.com/python-interface/#java">Java</a></li>
<li><a href="https://realpython.com/python-interface/#c">C++</a></li>
<li><a href="https://realpython.com/python-interface/#go">Go</a></li>
</ul>
</li>
<li><a href="https://realpython.com/python-interface/#conclusion">Conclusion</a></li>
</ul>
</div>
</div>
<div class="sidebar-module sidebar-module-inset text-center my-3 py-0">
<span>
<a target="_blank" rel="nofollow" href="https://twitter.com/intent/tweet/?text=Check%20out%20this%20%23Python%20tutorial:%20Implementing%20an%20Interface%20in%20Python%20by%20@realpython&amp;url=https%3A//realpython.com/python-interface/" class="mr-1 badge badge-twitter text-light mb-1"><i class="mr-1 fa fa-twitter text-light"></i>Tweet</a>
<a target="_blank" rel="nofollow" href="https://facebook.com/sharer/sharer.php?u=https%3A//realpython.com/python-interface/" class="mr-1 badge badge-facebook text-light mb-1"><i class="mr-1 fa fa-facebook text-light"></i>Share</a>
<a target="_blank" rel="nofollow" href="mailto:?subject=Python%20article%20for%20you&amp;body=Check%20out%20this%20Python%20tutorial:%0A%0AImplementing%20an%20Interface%20in%20Python%0A%0Ahttps%3A//realpython.com/python-interface/" class="mr-1 badge badge-red text-light mb-1"><i class="mr-1 fa fa-envelope text-light"></i>Email</a>
</span>
</div>
<div class="sidebar-module sidebar-module-inset p-0" style="overflow:hidden;">
<div style="display:block;position:relative;">
<div style="display:block;width:100%;padding-top:25%;"></div>
<div class="rpad" data-unit="4x1" style="position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;"><a href="https://srv.realpython.net/click/43555883729/?c=10466391474&amp;p=58946116052&amp;r=99256" rel="nofollow" target="_blank"><img src="./Request_files/1e343db533d77c15c03a534a86d34a0c" style="max-width: 100%; max-height: 100%; width: 100%;"></a></div>
</div>
</div>
</div>
</aside>
</div>
</div>
<div class="modal fade" id="modal-python-mastery-course" tabindex="-1" role="dialog" aria-hidden="true">
<div class="modal-dialog modal-dialog-centered modal-lg" role="document">
<div class="modal-content">
<div class="modal-header bg-light pt-3 pb-2">
<div class="container-fluid">
<div class="row">
<div class="col-12">
<div class="progress" style="height: .5rem;">
<div class="progress-bar progress-bar-striped progress-bar-animated w-50" role="progressbar"></div>
</div>
</div>
<div class="col-12">
<p class="text-muted text-center mb-0 mt-2">Almost there! Complete this form and click the button below to gain instant access:</p>
</div>
</div>
</div>
<button type="button" class="close" data-dismiss="modal" aria-label="Close">
<span aria-hidden="true">×</span>
</button>
</div>
<div class="modal-body m-4">
<div class="container-fluid">
<div class="row align-items-center">
<div class="col-12 col-lg-4">
<img class="img-fluid rounded w-100 mb-4" src="./Request_files/python-logo.webp">
</div>
<div class="col">
<p class="text-center h3 mb-4">5 Thoughts On Python Mastery</p>
<form class="col-12" action="https://realpython.com/optins/process/" method="post">
<input type="hidden" name="csrfmiddlewaretoken" value="ot8OKZL0ue2HgloPnd6ooKWJydPOUqQG4SGH3KGjsc7SOTOSruNNJO3N5KmF76zo">
<input type="hidden" name="slug" value="python-mastery-course">
<div class="form-group">
<input type="email" name="email" class="form-control" placeholder="Email Address" required="" autofocus="">
</div>
<button name="submit" type="submit" class="btn btn-primary btn-block text-wrap">Start the Class »</button>
</form>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<footer class="footer">
<div class="container">
<p class="text-center text-muted">© 2012–2020 Real Python ⋅ <a href="https://realpython.com/newsletter/">Newsletter</a> ⋅ <a href="https://www.youtube.com/realpython">YouTube</a> ⋅ <a href="https://twitter.com/realpython">Twitter</a> ⋅ <a href="https://facebook.com/LearnRealPython">Facebook</a> ⋅ <a href="https://www.instagram.com/realpython/">Instagram</a><br><a href="https://realpython.com/">Python Tutorials</a> ⋅ <a href="https://realpython.com/search">Search</a> ⋅ <a href="https://realpython.com/privacy-policy/">Privacy Policy</a> ⋅ <a href="https://realpython.com/energy-policy/" class="text-success active">Energy Policy</a> ⋅ <a href="https://realpython.com/sponsorships/">Advertise</a> ⋅ <a href="https://realpython.com/contact/">Contact</a><br>❤️ Happy Pythoning!</p>
</div>
</footer>
<script>
      (function(document, history, location) {
        var HISTORY_SUPPORT = !!(history && history.pushState);

        var anchorScrolls = {
          ANCHOR_REGEX: /^#[^ ]+$/,
          OFFSET_HEIGHT_PX: 120,

          /**
           * Establish events, and fix initial scroll position if a hash is provided.
           */
          init: function() {
            this.scrollToCurrent();
            window.addEventListener('hashchange', this.scrollToCurrent.bind(this));
            document.body.addEventListener('click', this.delegateAnchors.bind(this));
          },

          /**
           * Return the offset amount to deduct from the normal scroll position.
           * Modify as appropriate to allow for dynamic calculations
           */
          getFixedOffset: function() {
            return this.OFFSET_HEIGHT_PX;
          },

          /**
           * If the provided href is an anchor which resolves to an element on the
           * page, scroll to it.
           * @param  {String} href
           * @return {Boolean} - Was the href an anchor.
           */
          scrollIfAnchor: function(href, pushToHistory) {
            var match, rect, anchorOffset;

            if(!this.ANCHOR_REGEX.test(href)) {
              return false;
            }

            match = document.getElementById(href.slice(1));

            if(match) {
              rect = match.getBoundingClientRect();
              anchorOffset = window.pageYOffset + rect.top - this.getFixedOffset();
              window.scrollTo(window.pageXOffset, anchorOffset);

              // Add the state to history as-per normal anchor links
              if(HISTORY_SUPPORT && pushToHistory) {
                history.pushState({}, document.title, location.pathname + href);
              }
            }

            return !!match;
          },

          /**
           * Attempt to scroll to the current location's hash.
           */
          scrollToCurrent: function() {
            this.scrollIfAnchor(window.location.hash);
          },

          /**
           * If the click event's target was an anchor, fix the scroll position.
           */
          delegateAnchors: function(e) {
            var elem = e.target;

            if(
              elem.nodeName === 'A' &&
              this.scrollIfAnchor(elem.getAttribute('href'), true)
            ) {
              e.preventDefault();
            }
          }
        };

        window.addEventListener(
          'DOMContentLoaded', anchorScrolls.init.bind(anchorScrolls)
        );
      })(window.document, window.history, window.location);
    </script>
<script src="./Request_files/jquery.min.220afd743d9e.js"></script>
<script src="./Request_files/popper.min.1022eaf388cc.js"></script>
<script src="./Request_files/bootstrap.min.61f338f870fc.js"></script>
<script src="./Request_files/repl-toggle.366cb6d72340.js"></script>
<script>window.rp_prop_id = '58946116052';</script>
<script src="./Request_files/tag.js" async=""></script>
<script src="./Request_files/2153.js"></script>
<script>
  (function() {
    function throttle(a, b) { var c, d; return function () { var e = this, f = arguments, g = +new Date; c && g < c + a ? (clearTimeout(d), d = setTimeout(function () { c = g, b.apply(e, f) }, a)) : (c = g, b.apply(e, f)) } }
    var elems = document.getElementsByClassName("js-needs-scaling");
    var resizeAll = function() {
      Array.prototype.forEach.call(elems, function(elem) {
        var frames = elem.getElementsByTagName("iframe")
        if (frames.length === 0) {
          return;
        }
        var disclosure = elem.getElementsByClassName("js-disclosure");
        if (disclosure.length > 0) {
          disclosure[0].style.display = "";
        } else {
          disclosure[0].style.display = "none";
        }
        if (frames[0].clientWidth <= elem.parentElement.clientWidth) {
          elem.style.transform = "";
          elem.classList.add("text-center");
          return;
        }
        elem.classList.remove("text-center");
        elem.style.transform = "scale(" + elem.clientWidth / frames[0].width + ")";
      });
    }
    var periodicResize = function() {
      resizeAll();
      setTimeout(periodicResize, 100);
    }
    setTimeout(periodicResize, 100);
  })();
  </script>
<script id="dsq-count-scr" src="./Request_files/count.js" async=""></script>
<script>
      var disqus_config = function () {
        this.page.url = 'https://realpython.com/python-interface/';
        this.page.identifier = 'https://realpython.com/python-interface/';
        this.callbacks.onReady = [function() {
          if (window.onDisqusReady) {
            window.onDisqusReady();
          }
        }];
      };
      var disqus_script_url = 'https://realpython.disqus.com/embed.js';
    </script>
<script src="./Request_files/lazydisqus.3a3e39583b32.js" defer=""></script>
<script src="./Request_files/OneSignalSDK.js" async=""></script>
<script>
    var OneSignal = window.OneSignal || [];
    OneSignal.push(function() {
      OneSignal.init({
        appId: "c0081e20-a523-42bb-b0ac-04c5a9e8bf40"
      });
    });
  </script>
<script src="./Request_files/articlevc.11f8c3a3f08d.js" defer=""></script>
<script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "Article",
    "headline": "Implementing an Interface in Python",
    
    "image": {
      "@type": "ImageObject",
      "url": "https://files.realpython.com/media/Interfaces-in-Python_Watermarked.f9ce5bda238c.jpg",
      "width": 1920,
      "height": 1080
    },
    
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://realpython.com/python-interface/"
    },
    "datePublished": "2020-02-10T14:00:00+00:00",
    "dateModified": "2020-02-10T20:01:40.221669+00:00",
     "publisher": {
      "@type": "Organization",
      "name": "Real Python",
      "logo": {
        "@type": "ImageObject",
        "url": "https://realpython.com/static/real-python-logo-square-tiny.b2452b6d3823.png",
        "width": 60,
        "height": 60
      }
    },
    "author": {
      "@type": "Organization",
      "name": "Real Python",
      "url": "https://realpython.com",
      "logo": "https://realpython.com/static/real-python-logo-square.146e987bf77c.png"
    },
    "description": "In this tutorial, you&#39;ll explore how to use a Python interface. You&#39;ll come to understand why interfaces are so useful and learn how to implement formal and informal interfaces in Python. You&#39;ll also examine the differences between Python interfaces and those in other programming languages."
  }
  </script>
<script>
  var _dcq = _dcq || [];
  var _dcs = _dcs || {};
  _dcs.account = '6214500';

  (function() {
    var dc = document.createElement('script');
    dc.type = 'text/javascript'; dc.async = true;
    dc.src = '//tag.getdrip.com/6214500.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(dc, s);
  })();
</script>
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', '2220911568135371');
  fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=2220911568135371&ev=PageView&noscript=1"
/></noscript>


<iframe src="./Request_files/webPushAnalytics.html" style="display: none;"></iframe><div class="drip-tab-container">
  <div id="drip-106703" class="drip-tab side-image image-left mobile">
    <div id="drip-header-106703" class="drip-header">
      <a href="https://realpython.com/python-interface/#" id="drip-toggle-106703" class="drip-toggle">
        <h2 id="drip-teaser-106703">Improve Your Python</h2>
        <span id="drip-tab-up-106703" class="drip-arrow up">
          <svg width="12px" height="8px" viewBox="1362 659 12 8" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <polygon id="right_angle" stroke="none" fill="#FFFFFF" fill-rule="evenodd" transform="translate(1368.000000, 662.703125) rotate(-90.000000) translate(-1368.000000, -662.703125) " points="1364.29688 667.296875 1368.89062 662.703125 1364.29688 658.109375 1365.70312 656.703125 1371.70312 662.703125 1365.70312 668.703125"></polygon>
          </svg>
        </span>
        <span id="drip-tab-down-106703" class="drip-arrow down" style="display: none"></span>
      </a>
    </div>
    <div id="drip-content-106703" class="drip-content drip-clearfix" style="height: auto; bottom: -342px;">
      <a id="drip-close-106703" class="drip-close">
        <svg width="12px" height="12px" viewBox="630 19 12 12" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <polygon id="x" stroke="none" fill="#A8ACB9" fill-rule="evenodd" points="641.376687 30.1740899 636.49366 24.436669 641.095466 19 639.510399 19 635.701126 23.6038176 631.866288 19 630.281221 19 634.883028 24.436669 630 30.1740899 631.585067 30.1740899 635.701126 25.2463857 639.791621 30.1740899"></polygon>
        </svg>
      </a>

      <div id="drip-form-panel-106703" class="drip-panel drip-clearfix" style="display: block;">
        
          <div class="drip-form-aside">
            <span class="drip-image-helper"></span>
            <img src="./Request_files/side_ded3082af3893736e51b0d2da53701b6.png" class="drip-image">
          </div>
        

        <div class="drip-form-main">
          <h3 id="drip-content-header-106703">Improve Your Python</h3>
          
            <div id="drip-scroll-106703" class="drip-scroll">
          
            <div class="drip-description">...with a fresh 🐍&nbsp;<strong>Python&nbsp;Trick</strong>&nbsp;💌 &nbsp;<br>
code snippet every couple of days:</div>
            <form id="drip-form-106703">
              <div style="display: none">
                <input type="hidden" name="form_id" value="106703">
              </div>
              <dl class="no-labels">
                
                  
                    <dt>Email Address</dt>
                    <dd>
                      
                        <input type="email" name="fields[email]" value="" placeholder="Email Address" class="drip-text-field">
                        <div id="drip-errors-for-email-106703" class="drip-errors"></div>
                      
                    </dd>
                  
                
                  
                    <dt></dt>
                    <dd>
                      
                        <div class="zenput zenput--checkbox hidden" data-container="eu-checkbox">
                          <input type="hidden" name="fields[eu_consent]" id="drip-field-eu_consent-106703-denied" value="denied" disabled="disabled">
                          <input type="checkbox" name="fields[eu_consent]" id="drip-field-eu_consent-106703" value="granted" disabled="disabled">
                          <label class="zenput__checkbox-label" for="drip-field-eu_consent-106703">Receive the Real Python newsletter and get notified about new tutorials we publish on the site, as well as occasional special offers.
                            <div class="zenput__checkbox-label__icon"><svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg></div>
                          </label>
                        </div>
                      
                    </dd>
                  
                
                  
                    <input type="hidden" name="fields[eu_consent_message]" value="Receive the Real Python newsletter and get notified about new tutorials we publish on the site, as well as occasional special offers.">
                  
                
                
                <div style="display: none;" aria-hidden="true">
                  <dt for="website">Website</dt>
                  <dd>
                    <input type="text" id="website" name="website" placeholder="Website" class="drip-text-field" tabindex="-1" autocomplete="false" value="">
                  </dd>
                </div>
              </dl>
              <div class="form-controls">
                <input type="submit" name="submit" value="Send Python Tricks »" id="drip-submit-106703" class="drip-submit-button">
              </div>
            </form>
          </div>
        </div>
      </div>

      <div id="drip-success-panel-106703" class="drip-success drip-panel drip-clearfix" style="display: none">
        <h3>Almost there...</h3>
        <p class="drip-description drip-post-submission">Check your inbox. I'm sending you the first Python Trick right now.</p>
      </div>

      
    </div>
  </div>
</div><div class="drip-lightbox-wrapper">
  <div id="drip-108609" class="drip-lightbox drip-hidden side-image image-right mobile">
    <div id="drip-content-108609" class="drip-content" style="height: auto; bottom: -50px;">
      <a id="drip-close-108609" class="drip-close">
        <svg width="12px" height="12px" viewBox="630 19 12 12" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <polygon id="x" stroke="none" fill="#A8ACB9" fill-rule="evenodd" points="641.376687 30.1740899 636.49366 24.436669 641.095466 19 639.510399 19 635.701126 23.6038176 631.866288 19 630.281221 19 634.883028 24.436669 630 30.1740899 631.585067 30.1740899 635.701126 25.2463857 639.791621 30.1740899"></polygon>
        </svg>
      </a>

      <div id="drip-form-panel-108609" class="drip-panel" style="display: block;">
        
          <div class="drip-form-aside">
            <span class="drip-image-helper"></span>
            <img src="./Request_files/side_0743418fd26dda9240db39b8bc3744e1.png" class="drip-image">
          </div>
        

        <div class="drip-form-main">
          <h3 id="drip-content-header-108609">Get the Python Cheat Sheet</h3>
          
            <div id="drip-scroll-108609" class="drip-scroll">
          
            <div class="drip-description">Enter your email address below and we'll send you the Python cheat sheet right away:</div>

            <form id="drip-form-108609">
              <dl class="no-labels">
                
                  
                    
                      <dt>Email Address</dt>
                    
                    <dd>
                      
                        <input type="email" name="fields[email]" value="" placeholder="Email Address" class="drip-text-field">
                        <div id="drip-errors-for-email-108609" class="drip-errors"></div>
                      
                    </dd>
                  
                
                  
                    
                    <dd>
                      
                        <div class="zenput zenput--checkbox hidden" data-container="eu-checkbox">
                          <input type="hidden" name="fields[eu_consent]" id="drip-field-eu_consent-108609-denied" value="denied" disabled="disabled">
                          <input type="checkbox" name="fields[eu_consent]" id="drip-field-eu_consent-108609" value="granted" disabled="disabled">
                          <label class="zenput__checkbox-label" for="drip-field-eu_consent-108609">Receive the Real Python newsletter and get notified about new tutorials we publish on the site, as well as occasional special offers.
                            <div class="zenput__checkbox-label__icon"><svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg></div>
                          </label>
                        </div>
                      
                    </dd>
                  
                
                  
                    <input type="hidden" name="fields[eu_consent_message]" value="Receive the Real Python newsletter and get notified about new tutorials we publish on the site, as well as occasional special offers.">
                  
                
                
                <div style="display: none;" aria-hidden="true">
                  <dt for="website">Website</dt>
                  <dd>
                    <input type="text" id="website" name="website" placeholder="Website" class="drip-text-field" tabindex="-1" autocomplete="false" value="">
                  </dd>
                </div>
              </dl>
              <div class="form-controls">
                <input type="submit" name="submit" value="Send My Python Cheat Sheet »" id="drip-submit-108609" class="drip-submit-button">
              </div>
            </form>
          </div>
        </div>
      </div>

      <div id="drip-success-panel-108609" class="drip-success drip-panel" style="display: none">
        <h3>Almost there...</h3>
        <p class="drip-description drip-post-submission">We emailed you the cheat sheet. Please check your inbox in a few minutes.</p>
      </div>

      
    </div>
  </div>
  <div id="drip-backdrop-108609" class="drip-backdrop drip-fade drip-hidden"></div>
</div><div class="drip-lightbox-wrapper">
  <div id="drip-108599" class="drip-lightbox drip-hidden side-image image-right mobile">
    <div id="drip-content-108599" class="drip-content" style="height: auto; bottom: -50px;">
      <a id="drip-close-108599" class="drip-close">
        <svg width="12px" height="12px" viewBox="630 19 12 12" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <polygon id="x" stroke="none" fill="#A8ACB9" fill-rule="evenodd" points="641.376687 30.1740899 636.49366 24.436669 641.095466 19 639.510399 19 635.701126 23.6038176 631.866288 19 630.281221 19 634.883028 24.436669 630 30.1740899 631.585067 30.1740899 635.701126 25.2463857 639.791621 30.1740899"></polygon>
        </svg>
      </a>

      <div id="drip-form-panel-108599" class="drip-panel" style="display: block;">
        
          <div class="drip-form-aside">
            <span class="drip-image-helper"></span>
            <img src="./Request_files/side_c058822f7c534cad01d5dea43398e2fd.png" class="drip-image">
          </div>
        

        <div class="drip-form-main">
          <h3 id="drip-content-header-108599">Get a Sample Chapter From the First Course</h3>
          
            <div id="drip-scroll-108599" class="drip-scroll">
          
            <div class="drip-description">Enter your email address below and we'll send you the sample chapter right away:</div>

            <form id="drip-form-108599">
              <dl class="no-labels">
                
                  
                    
                      <dt>Email Address</dt>
                    
                    <dd>
                      
                        <input type="email" name="fields[email]" value="" placeholder="Email Address" class="drip-text-field">
                        <div id="drip-errors-for-email-108599" class="drip-errors"></div>
                      
                    </dd>
                  
                
                  
                    
                    <dd>
                      
                        <div class="zenput zenput--checkbox hidden" data-container="eu-checkbox">
                          <input type="hidden" name="fields[eu_consent]" id="drip-field-eu_consent-108599-denied" value="denied" disabled="disabled">
                          <input type="checkbox" name="fields[eu_consent]" id="drip-field-eu_consent-108599" value="granted" disabled="disabled">
                          <label class="zenput__checkbox-label" for="drip-field-eu_consent-108599">Receive the Real Python newsletter and get notified about new tutorials we publish on the site, as well as occasional special offers.
                            <div class="zenput__checkbox-label__icon"><svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg></div>
                          </label>
                        </div>
                      
                    </dd>
                  
                
                  
                    <input type="hidden" name="fields[eu_consent_message]" value="Receive the Real Python newsletter and get notified about new tutorials we publish on the site, as well as occasional special offers.">
                  
                
                
                <div style="display: none;" aria-hidden="true">
                  <dt for="website">Website</dt>
                  <dd>
                    <input type="text" id="website" name="website" placeholder="Website" class="drip-text-field" tabindex="-1" autocomplete="false" value="">
                  </dd>
                </div>
              </dl>
              <div class="form-controls">
                <input type="submit" name="submit" value="Get Sample Chapter »" id="drip-submit-108599" class="drip-submit-button">
              </div>
            </form>
          </div>
        </div>
      </div>

      <div id="drip-success-panel-108599" class="drip-success drip-panel" style="display: none">
        <h3>Almost there...</h3>
        <p class="drip-description drip-post-submission">We emailed you the sample chapter. Please check your inbox in a few minutes.</p>
      </div>

      
    </div>
  </div>
  <div id="drip-backdrop-108599" class="drip-backdrop drip-fade drip-hidden"></div>
</div><div id="onesignal-bell-container" class="onesignal-bell-container onesignal-reset onesignal-bell-container-bottom-left"><div id="onesignal-bell-launcher" class="onesignal-bell-launcher onesignal-bell-launcher-md onesignal-bell-launcher-bottom-left onesignal-bell-launcher-theme-default onesignal-bell-launcher-active" style="bottom: 15px; left: 15px;"><div class="onesignal-bell-launcher-button"><svg class="onesignal-bell-svg" xmlns="http://www.w3.org/2000/svg" width="99.7" height="99.7" viewBox="0 0 99.7 99.7" style="filter: drop-shadow(0 2px 4px rgba(34,36,38,0.35));; -webkit-filter: drop-shadow(0 2px 4px rgba(34,36,38,0.35));;"><circle class="background" cx="49.9" cy="49.9" r="49.9" style="fill: rgb(208, 2, 27);"></circle><path class="foreground" d="M50.1 66.2H27.7s-2-.2-2-2.1c0-1.9 1.7-2 1.7-2s6.7-3.2 6.7-5.5S33 52.7 33 43.3s6-16.6 13.2-16.6c0 0 1-2.4 3.9-2.4 2.8 0 3.8 2.4 3.8 2.4 7.2 0 13.2 7.2 13.2 16.6s-1 11-1 13.3c0 2.3 6.7 5.5 6.7 5.5s1.7.1 1.7 2c0 1.8-2.1 2.1-2.1 2.1H50.1zm-7.2 2.3h14.5s-1 6.3-7.2 6.3-7.3-6.3-7.3-6.3z" style="fill: rgb(255, 255, 255);"></path><ellipse class="stroke" cx="49.9" cy="49.9" rx="37.4" ry="36.9" style="stroke: rgb(255, 255, 255);"></ellipse></svg></div><div class="onesignal-bell-launcher-badge" style="filter: drop-shadow(0 2px 4px rgba(34,36,38,0));; -webkit-filter: drop-shadow(0 2px 4px rgba(34,36,38,0));;"></div><div class="onesignal-bell-launcher-message"><div class="onesignal-bell-launcher-message-body"></div></div><div class="onesignal-bell-launcher-dialog" style="filter: drop-shadow(0px 2px 2px rgba(34,36,38,.15));; -webkit-filter: drop-shadow(0px 2px 2px rgba(34,36,38,.15));;"><div class="onesignal-bell-launcher-dialog-body"></div></div></div></div><iframe id="google_osd_static_frame_4082085504073" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;" src="./Request_files/saved_resource(1).html"></iframe></body><iframe sandbox="allow-scripts allow-same-origin" id="35b2040a6082652" frameborder="0" allowtransparency="true" marginheight="0" marginwidth="0" width="0" hspace="0" vspace="0" height="0" style="height:0px;width:0px;display:none;" scrolling="no" src="./Request_files/cs(1).html">
    </iframe></html>