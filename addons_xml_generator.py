



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = "ABZ6GAelVFkqf4ROpDtWudp5VAxYAtD3tg:1434808271687";
 
 
 var CS_env = {"domainName": null, "projectHomeUrl": "/p/repository-xbmcmania", "relativeBaseUrl": "", "loggedInUserEmail": "salondigitalpedidos@gmail.com", "assetHostPath": "https://ssl.gstatic.com/codesite/ph", "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/8599073060794244502", "projectName": "repository-xbmcmania", "profileUrl": "/u/107543989748942104600/", "token": "ABZ6GAelVFkqf4ROpDtWudp5VAxYAtD3tg:1434808271687"};
 var _gaq = _gaq || [];
 _gaq.push(
 ['siteTracker._setAccount', 'UA-18071-1'],
 ['siteTracker._trackPageview']);
 
 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
 })();
 
 </script>
 
 
 <title>addons_xml_generator.py - 
 repository-xbmcmania -
 
 
 repository-xbmcmania - Google Project Hosting
 </title>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/8599073060794244502/css/core.css">
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/8599073060794244502/css/ph_detail.css" >
 
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/8599073060794244502/css/d_sb.css" >
 
 
 
<!--[if IE]>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/8599073060794244502/css/d_ie.css" >
<![endif]-->
 <style type="text/css">
 .menuIcon.off { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -42px }
 .menuIcon.on { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -28px }
 .menuIcon.down { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 0; }
 
 
 
  tr.inline_comment {
 background: #fff;
 vertical-align: top;
 }
 div.draft, div.published {
 padding: .3em;
 border: 1px solid #999; 
 margin-bottom: .1em;
 font-family: arial, sans-serif;
 max-width: 60em;
 }
 div.draft {
 background: #ffa;
 } 
 div.published {
 background: #e5ecf9;
 }
 div.published .body, div.draft .body {
 padding: .5em .1em .1em .1em;
 max-width: 60em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
 font-size: 1em;
 }
 div.draft .actions {
 margin-left: 1em;
 font-size: 90%;
 }
 div.draft form {
 padding: .5em .5em .5em 0;
 }
 div.draft textarea, div.published textarea {
 width: 95%;
 height: 10em;
 font-family: arial, sans-serif;
 margin-bottom: .5em;
 }

 
 .nocursor, .nocursor td, .cursor_hidden, .cursor_hidden td {
 background-color: white;
 height: 2px;
 }
 .cursor, .cursor td {
 background-color: darkblue;
 height: 2px;
 display: '';
 }
 
 
.list {
 border: 1px solid white;
 border-bottom: 0;
}

 
 </style>
</head>
<body class="t4">
<script type="text/javascript">
 window.___gcfg = {lang: 'en'};
 (function() 
 {var po = document.createElement("script");
 po.type = "text/javascript"; po.async = true;po.src = "https://apis.google.com/js/plusone.js";
 var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(po, s);
 })();
</script>
<div class="headbg">

 <div id="gaia">
 

 <span>
 
 
 
 <a href="#" id="multilogin-dropdown" onclick="return false;"
 ><u><b>salondigitalpedidos@gmail.com</b></u> <small>&#9660;</small></a>
 
 
 | <a href="/u/107543989748942104600/" id="projects-dropdown" onclick="return false;"
 ><u>My favorites</u> <small>&#9660;</small></a>
 | <a href="/u/107543989748942104600/" onclick="_CS_click('/gb/ph/profile');"
 title="Profile, Updates, and Settings"
 ><u>Profile</u></a>
 | <a href="https://www.google.com/accounts/Logout?continue=https%3A%2F%2Fcode.google.com%2Fp%2Frepository-xbmcmania%2Fsource%2Fbrowse%2Ftrunk%2FHelix%2Faddons_xml_generator.py" 
 onclick="_CS_click('/gb/ph/signout');"
 ><u>Sign out</u></a>
 
 </span>

 </div>

 <div class="gbh" style="left: 0pt;"></div>
 <div class="gbh" style="right: 0pt;"></div>
 
 
 <div style="height: 1px"></div>
<!--[if lte IE 7]>
<div style="text-align:center;">
Your version of Internet Explorer is not supported. Try a browser that
contributes to open source, such as <a href="http://www.firefox.com">Firefox</a>,
<a href="http://www.google.com/chrome">Google Chrome</a>, or
<a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.
</div>
<![endif]-->



 <table style="padding:0px; margin: 0px 0px 10px 0px; width:100%" cellpadding="0" cellspacing="0"
 itemscope itemtype="http://schema.org/CreativeWork">
 <tr style="height: 58px;">
 
 
 
 <td id="plogo">
 <link itemprop="url" href="/p/repository-xbmcmania">
 <a href="/p/repository-xbmcmania/">
 
 
 <img src="/p/repository-xbmcmania/logo?cct=1420473224"
 alt="Logo" itemprop="image">
 
 </a>
 </td>
 
 <td style="padding-left: 0.5em">
 
 <div id="pname">
 <a href="/p/repository-xbmcmania/"><span itemprop="name">repository-xbmcmania</span></a>
 </div>
 
 <div id="psum">
 <a id="project_summary_link"
 href="/p/repository-xbmcmania/"><span itemprop="description">repository-xbmcmania</span></a>
 
 </div>
 
 
 </td>
 <td style="white-space:nowrap;text-align:right; vertical-align:bottom;">
 
 <form action="/hosting/search">
 <input size="30" name="q" value="" type="text">
 
 <input type="submit" name="projectsearch" value="Search projects" >
 </form>
 
 </tr>
 </table>

</div>

 
<div id="mt" class="gtb"> 
 <a href="/p/repository-xbmcmania/" class="tab ">Project&nbsp;Home</a>
 
 
 
 
 
 
 <a href="/p/repository-xbmcmania/w/list" class="tab ">Wiki</a>
 
 
 
 
 
 <a href="/p/repository-xbmcmania/issues/list"
 class="tab ">Issues</a>
 
 
 
 
 
 <a href="/p/repository-xbmcmania/source/checkout"
 class="tab active">Source</a>
 
 
 
 
 
 
 
 
 <a href="https://code.google.com/export-to-github/export?project=repository-xbmcmania">
 <button>Export to GitHub</button>
 
 </a>
 
 
 
 
 
 <div class=gtbc></div>
</div>
<table cellspacing="0" cellpadding="0" width="100%" align="center" border="0" class="st">
 <tr>
 
 
 
 
 
 
 <td class="subt">
 <div class="st2">
 <div class="isf">
 
 


 <span class="inst1"><a href="/p/repository-xbmcmania/source/checkout">Checkout</a></span> &nbsp;
 <span class="inst2"><a href="/p/repository-xbmcmania/source/browse/">Browse</a></span> &nbsp;
 <span class="inst3"><a href="/p/repository-xbmcmania/source/list">Changes</a></span> &nbsp;
 
 
 
 
 
 
 
 </form>
 <script type="text/javascript">
 
 function codesearchQuery(form) {
 var query = document.getElementById('q').value;
 if (query) { form.action += '%20' + query; }
 }
 </script>
 </div>
</div>

 </td>
 
 
 
 <td align="right" valign="top" class="bevel-right"></td>
 </tr>
</table>


<script type="text/javascript">
 var cancelBubble = false;
 function _go(url) { document.location = url; }
</script>
<div id="maincol"
 
>

 




<div class="expand">
<div id="colcontrol">
<style type="text/css">
 #file_flipper { white-space: nowrap; padding-right: 2em; }
 #file_flipper.hidden { display: none; }
 #file_flipper .pagelink { color: #0000CC; text-decoration: underline; }
 #file_flipper #visiblefiles { padding-left: 0.5em; padding-right: 0.5em; }
</style>
<table id="nav_and_rev" class="list"
 cellpadding="0" cellspacing="0" width="100%">
 <tr>
 
 <td nowrap="nowrap" class="src_crumbs src_nav" width="33%">
 <strong class="src_nav">Source path:&nbsp;</strong>
 <span id="crumb_root">
 
 <a href="/p/repository-xbmcmania/source/browse/">svn</a>/&nbsp;</span>
 <span id="crumb_links" class="ifClosed"><a href="/p/repository-xbmcmania/source/browse/trunk/">trunk</a><span class="sp">/&nbsp;</span><a href="/p/repository-xbmcmania/source/browse/trunk/Helix/">Helix</a><span class="sp">/&nbsp;</span>addons_xml_generator.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="center">
 <a href="/p/repository-xbmcmania/source/browse/trunk/Helix/addons_xml_generator.py?edit=1"
 ><img src="https://ssl.gstatic.com/codesite/ph/images/pencil-y14.png"
 class="edit_icon">Edit file</a>
 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper"><b>r11</b></td>
 
 </tr></table>
 </td> 
 </tr>
</table>

<div class="fc">
 
 
 
<style type="text/css">
.undermouse span {
 background-image: url(https://ssl.gstatic.com/codesite/ph/images/comments.gif); }
</style>
<table class="opened" id="review_comment_area"
><tr>
<td id="nums">
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
<pre><table width="100%" id="nums_table_0"><tr id="gr_svn11_1"

><td id="1"><a href="#1">1</a></td></tr
><tr id="gr_svn11_2"

><td id="2"><a href="#2">2</a></td></tr
><tr id="gr_svn11_3"

><td id="3"><a href="#3">3</a></td></tr
><tr id="gr_svn11_4"

><td id="4"><a href="#4">4</a></td></tr
><tr id="gr_svn11_5"

><td id="5"><a href="#5">5</a></td></tr
><tr id="gr_svn11_6"

><td id="6"><a href="#6">6</a></td></tr
><tr id="gr_svn11_7"

><td id="7"><a href="#7">7</a></td></tr
><tr id="gr_svn11_8"

><td id="8"><a href="#8">8</a></td></tr
><tr id="gr_svn11_9"

><td id="9"><a href="#9">9</a></td></tr
><tr id="gr_svn11_10"

><td id="10"><a href="#10">10</a></td></tr
><tr id="gr_svn11_11"

><td id="11"><a href="#11">11</a></td></tr
><tr id="gr_svn11_12"

><td id="12"><a href="#12">12</a></td></tr
><tr id="gr_svn11_13"

><td id="13"><a href="#13">13</a></td></tr
><tr id="gr_svn11_14"

><td id="14"><a href="#14">14</a></td></tr
><tr id="gr_svn11_15"

><td id="15"><a href="#15">15</a></td></tr
><tr id="gr_svn11_16"

><td id="16"><a href="#16">16</a></td></tr
><tr id="gr_svn11_17"

><td id="17"><a href="#17">17</a></td></tr
><tr id="gr_svn11_18"

><td id="18"><a href="#18">18</a></td></tr
><tr id="gr_svn11_19"

><td id="19"><a href="#19">19</a></td></tr
><tr id="gr_svn11_20"

><td id="20"><a href="#20">20</a></td></tr
><tr id="gr_svn11_21"

><td id="21"><a href="#21">21</a></td></tr
><tr id="gr_svn11_22"

><td id="22"><a href="#22">22</a></td></tr
><tr id="gr_svn11_23"

><td id="23"><a href="#23">23</a></td></tr
><tr id="gr_svn11_24"

><td id="24"><a href="#24">24</a></td></tr
><tr id="gr_svn11_25"

><td id="25"><a href="#25">25</a></td></tr
><tr id="gr_svn11_26"

><td id="26"><a href="#26">26</a></td></tr
><tr id="gr_svn11_27"

><td id="27"><a href="#27">27</a></td></tr
><tr id="gr_svn11_28"

><td id="28"><a href="#28">28</a></td></tr
><tr id="gr_svn11_29"

><td id="29"><a href="#29">29</a></td></tr
><tr id="gr_svn11_30"

><td id="30"><a href="#30">30</a></td></tr
><tr id="gr_svn11_31"

><td id="31"><a href="#31">31</a></td></tr
><tr id="gr_svn11_32"

><td id="32"><a href="#32">32</a></td></tr
><tr id="gr_svn11_33"

><td id="33"><a href="#33">33</a></td></tr
><tr id="gr_svn11_34"

><td id="34"><a href="#34">34</a></td></tr
><tr id="gr_svn11_35"

><td id="35"><a href="#35">35</a></td></tr
><tr id="gr_svn11_36"

><td id="36"><a href="#36">36</a></td></tr
><tr id="gr_svn11_37"

><td id="37"><a href="#37">37</a></td></tr
><tr id="gr_svn11_38"

><td id="38"><a href="#38">38</a></td></tr
><tr id="gr_svn11_39"

><td id="39"><a href="#39">39</a></td></tr
><tr id="gr_svn11_40"

><td id="40"><a href="#40">40</a></td></tr
><tr id="gr_svn11_41"

><td id="41"><a href="#41">41</a></td></tr
><tr id="gr_svn11_42"

><td id="42"><a href="#42">42</a></td></tr
><tr id="gr_svn11_43"

><td id="43"><a href="#43">43</a></td></tr
><tr id="gr_svn11_44"

><td id="44"><a href="#44">44</a></td></tr
><tr id="gr_svn11_45"

><td id="45"><a href="#45">45</a></td></tr
><tr id="gr_svn11_46"

><td id="46"><a href="#46">46</a></td></tr
><tr id="gr_svn11_47"

><td id="47"><a href="#47">47</a></td></tr
><tr id="gr_svn11_48"

><td id="48"><a href="#48">48</a></td></tr
><tr id="gr_svn11_49"

><td id="49"><a href="#49">49</a></td></tr
><tr id="gr_svn11_50"

><td id="50"><a href="#50">50</a></td></tr
><tr id="gr_svn11_51"

><td id="51"><a href="#51">51</a></td></tr
><tr id="gr_svn11_52"

><td id="52"><a href="#52">52</a></td></tr
><tr id="gr_svn11_53"

><td id="53"><a href="#53">53</a></td></tr
><tr id="gr_svn11_54"

><td id="54"><a href="#54">54</a></td></tr
><tr id="gr_svn11_55"

><td id="55"><a href="#55">55</a></td></tr
><tr id="gr_svn11_56"

><td id="56"><a href="#56">56</a></td></tr
><tr id="gr_svn11_57"

><td id="57"><a href="#57">57</a></td></tr
><tr id="gr_svn11_58"

><td id="58"><a href="#58">58</a></td></tr
><tr id="gr_svn11_59"

><td id="59"><a href="#59">59</a></td></tr
><tr id="gr_svn11_60"

><td id="60"><a href="#60">60</a></td></tr
><tr id="gr_svn11_61"

><td id="61"><a href="#61">61</a></td></tr
><tr id="gr_svn11_62"

><td id="62"><a href="#62">62</a></td></tr
><tr id="gr_svn11_63"

><td id="63"><a href="#63">63</a></td></tr
><tr id="gr_svn11_64"

><td id="64"><a href="#64">64</a></td></tr
><tr id="gr_svn11_65"

><td id="65"><a href="#65">65</a></td></tr
><tr id="gr_svn11_66"

><td id="66"><a href="#66">66</a></td></tr
><tr id="gr_svn11_67"

><td id="67"><a href="#67">67</a></td></tr
><tr id="gr_svn11_68"

><td id="68"><a href="#68">68</a></td></tr
><tr id="gr_svn11_69"

><td id="69"><a href="#69">69</a></td></tr
><tr id="gr_svn11_70"

><td id="70"><a href="#70">70</a></td></tr
><tr id="gr_svn11_71"

><td id="71"><a href="#71">71</a></td></tr
><tr id="gr_svn11_72"

><td id="72"><a href="#72">72</a></td></tr
><tr id="gr_svn11_73"

><td id="73"><a href="#73">73</a></td></tr
><tr id="gr_svn11_74"

><td id="74"><a href="#74">74</a></td></tr
><tr id="gr_svn11_75"

><td id="75"><a href="#75">75</a></td></tr
><tr id="gr_svn11_76"

><td id="76"><a href="#76">76</a></td></tr
><tr id="gr_svn11_77"

><td id="77"><a href="#77">77</a></td></tr
><tr id="gr_svn11_78"

><td id="78"><a href="#78">78</a></td></tr
><tr id="gr_svn11_79"

><td id="79"><a href="#79">79</a></td></tr
><tr id="gr_svn11_80"

><td id="80"><a href="#80">80</a></td></tr
><tr id="gr_svn11_81"

><td id="81"><a href="#81">81</a></td></tr
><tr id="gr_svn11_82"

><td id="82"><a href="#82">82</a></td></tr
><tr id="gr_svn11_83"

><td id="83"><a href="#83">83</a></td></tr
><tr id="gr_svn11_84"

><td id="84"><a href="#84">84</a></td></tr
><tr id="gr_svn11_85"

><td id="85"><a href="#85">85</a></td></tr
><tr id="gr_svn11_86"

><td id="86"><a href="#86">86</a></td></tr
><tr id="gr_svn11_87"

><td id="87"><a href="#87">87</a></td></tr
><tr id="gr_svn11_88"

><td id="88"><a href="#88">88</a></td></tr
><tr id="gr_svn11_89"

><td id="89"><a href="#89">89</a></td></tr
><tr id="gr_svn11_90"

><td id="90"><a href="#90">90</a></td></tr
><tr id="gr_svn11_91"

><td id="91"><a href="#91">91</a></td></tr
><tr id="gr_svn11_92"

><td id="92"><a href="#92">92</a></td></tr
><tr id="gr_svn11_93"

><td id="93"><a href="#93">93</a></td></tr
><tr id="gr_svn11_94"

><td id="94"><a href="#94">94</a></td></tr
><tr id="gr_svn11_95"

><td id="95"><a href="#95">95</a></td></tr
><tr id="gr_svn11_96"

><td id="96"><a href="#96">96</a></td></tr
><tr id="gr_svn11_97"

><td id="97"><a href="#97">97</a></td></tr
><tr id="gr_svn11_98"

><td id="98"><a href="#98">98</a></td></tr
><tr id="gr_svn11_99"

><td id="99"><a href="#99">99</a></td></tr
><tr id="gr_svn11_100"

><td id="100"><a href="#100">100</a></td></tr
><tr id="gr_svn11_101"

><td id="101"><a href="#101">101</a></td></tr
><tr id="gr_svn11_102"

><td id="102"><a href="#102">102</a></td></tr
><tr id="gr_svn11_103"

><td id="103"><a href="#103">103</a></td></tr
><tr id="gr_svn11_104"

><td id="104"><a href="#104">104</a></td></tr
><tr id="gr_svn11_105"

><td id="105"><a href="#105">105</a></td></tr
><tr id="gr_svn11_106"

><td id="106"><a href="#106">106</a></td></tr
><tr id="gr_svn11_107"

><td id="107"><a href="#107">107</a></td></tr
><tr id="gr_svn11_108"

><td id="108"><a href="#108">108</a></td></tr
><tr id="gr_svn11_109"

><td id="109"><a href="#109">109</a></td></tr
><tr id="gr_svn11_110"

><td id="110"><a href="#110">110</a></td></tr
><tr id="gr_svn11_111"

><td id="111"><a href="#111">111</a></td></tr
><tr id="gr_svn11_112"

><td id="112"><a href="#112">112</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svn11_1

><td class="source"># *<br></td></tr
><tr
id=sl_svn11_2

><td class="source"># *  Copyright (C) 2012-2013 Garrett Brown<br></td></tr
><tr
id=sl_svn11_3

><td class="source"># *  Copyright (C) 2010      j48antialias<br></td></tr
><tr
id=sl_svn11_4

><td class="source"># *<br></td></tr
><tr
id=sl_svn11_5

><td class="source"># *  This Program is free software; you can redistribute it and/or modify<br></td></tr
><tr
id=sl_svn11_6

><td class="source"># *  it under the terms of the GNU General Public License as published by<br></td></tr
><tr
id=sl_svn11_7

><td class="source"># *  the Free Software Foundation; either version 2, or (at your option)<br></td></tr
><tr
id=sl_svn11_8

><td class="source"># *  any later version.<br></td></tr
><tr
id=sl_svn11_9

><td class="source"># *<br></td></tr
><tr
id=sl_svn11_10

><td class="source"># *  This Program is distributed in the hope that it will be useful,<br></td></tr
><tr
id=sl_svn11_11

><td class="source"># *  but WITHOUT ANY WARRANTY; without even the implied warranty of<br></td></tr
><tr
id=sl_svn11_12

><td class="source"># *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the<br></td></tr
><tr
id=sl_svn11_13

><td class="source"># *  GNU General Public License for more details.<br></td></tr
><tr
id=sl_svn11_14

><td class="source"># *<br></td></tr
><tr
id=sl_svn11_15

><td class="source"># *  You should have received a copy of the GNU General Public License<br></td></tr
><tr
id=sl_svn11_16

><td class="source"># *  along with XBMC; see the file COPYING.  If not, write to<br></td></tr
><tr
id=sl_svn11_17

><td class="source"># *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.<br></td></tr
><tr
id=sl_svn11_18

><td class="source"># *  http://www.gnu.org/copyleft/gpl.html<br></td></tr
><tr
id=sl_svn11_19

><td class="source"># *<br></td></tr
><tr
id=sl_svn11_20

><td class="source"># *  Based on code by j48antialias:<br></td></tr
><tr
id=sl_svn11_21

><td class="source"># *  https://anarchintosh-projects.googlecode.com/files/addons_xml_generator.py<br></td></tr
><tr
id=sl_svn11_22

><td class="source"> <br></td></tr
><tr
id=sl_svn11_23

><td class="source">&quot;&quot;&quot; addons.xml generator &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svn11_24

><td class="source"> <br></td></tr
><tr
id=sl_svn11_25

><td class="source">import os<br></td></tr
><tr
id=sl_svn11_26

><td class="source">import sys<br></td></tr
><tr
id=sl_svn11_27

><td class="source"> <br></td></tr
><tr
id=sl_svn11_28

><td class="source"># Compatibility with 3.0, 3.1 and 3.2 not supporting u&quot;&quot; literals<br></td></tr
><tr
id=sl_svn11_29

><td class="source">if sys.version &lt; &#39;3&#39;:<br></td></tr
><tr
id=sl_svn11_30

><td class="source">    import codecs<br></td></tr
><tr
id=sl_svn11_31

><td class="source">    def u(x):<br></td></tr
><tr
id=sl_svn11_32

><td class="source">        return codecs.unicode_escape_decode(x)[0]<br></td></tr
><tr
id=sl_svn11_33

><td class="source">else:<br></td></tr
><tr
id=sl_svn11_34

><td class="source">    def u(x):<br></td></tr
><tr
id=sl_svn11_35

><td class="source">        return x<br></td></tr
><tr
id=sl_svn11_36

><td class="source"> <br></td></tr
><tr
id=sl_svn11_37

><td class="source">class Generator:<br></td></tr
><tr
id=sl_svn11_38

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svn11_39

><td class="source">        Generates a new addons.xml file from each addons addon.xml file<br></td></tr
><tr
id=sl_svn11_40

><td class="source">        and a new addons.xml.md5 hash file. Must be run from the root of<br></td></tr
><tr
id=sl_svn11_41

><td class="source">        the checked-out repo. Only handles single depth folder structure.<br></td></tr
><tr
id=sl_svn11_42

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svn11_43

><td class="source">    def __init__( self ):<br></td></tr
><tr
id=sl_svn11_44

><td class="source">        # generate files<br></td></tr
><tr
id=sl_svn11_45

><td class="source">        self._generate_addons_file()<br></td></tr
><tr
id=sl_svn11_46

><td class="source">        self._generate_md5_file()<br></td></tr
><tr
id=sl_svn11_47

><td class="source">        # notify user<br></td></tr
><tr
id=sl_svn11_48

><td class="source">        print(&quot;Finished updating addons xml and md5 files&quot;)<br></td></tr
><tr
id=sl_svn11_49

><td class="source"> <br></td></tr
><tr
id=sl_svn11_50

><td class="source">    def _generate_addons_file( self ):<br></td></tr
><tr
id=sl_svn11_51

><td class="source">        # addon list<br></td></tr
><tr
id=sl_svn11_52

><td class="source">        addons = os.listdir( &quot;.&quot; )<br></td></tr
><tr
id=sl_svn11_53

><td class="source">        # final addons text<br></td></tr
><tr
id=sl_svn11_54

><td class="source">        addons_xml = u(&quot;&lt;?xml version=\&quot;1.0\&quot; encoding=\&quot;UTF-8\&quot; standalone=\&quot;yes\&quot;?&gt;\n&lt;addons&gt;\n&quot;)<br></td></tr
><tr
id=sl_svn11_55

><td class="source">        # loop thru and add each addons addon.xml file<br></td></tr
><tr
id=sl_svn11_56

><td class="source">        for addon in addons:<br></td></tr
><tr
id=sl_svn11_57

><td class="source">            try:<br></td></tr
><tr
id=sl_svn11_58

><td class="source">                # skip any file or .svn folder or .git folder<br></td></tr
><tr
id=sl_svn11_59

><td class="source">                if ( not os.path.isdir( addon ) or addon == &quot;.svn&quot; or addon == &quot;.git&quot; ): continue<br></td></tr
><tr
id=sl_svn11_60

><td class="source">                # create path<br></td></tr
><tr
id=sl_svn11_61

><td class="source">                _path = os.path.join( addon, &quot;addon.xml&quot; )<br></td></tr
><tr
id=sl_svn11_62

><td class="source">                # split lines for stripping<br></td></tr
><tr
id=sl_svn11_63

><td class="source">                xml_lines = open( _path, &quot;r&quot; ).read().splitlines()<br></td></tr
><tr
id=sl_svn11_64

><td class="source">                # new addon<br></td></tr
><tr
id=sl_svn11_65

><td class="source">                addon_xml = &quot;&quot;<br></td></tr
><tr
id=sl_svn11_66

><td class="source">                # loop thru cleaning each line<br></td></tr
><tr
id=sl_svn11_67

><td class="source">                for line in xml_lines:<br></td></tr
><tr
id=sl_svn11_68

><td class="source">                    # skip encoding format line<br></td></tr
><tr
id=sl_svn11_69

><td class="source">                    if ( line.find( &quot;&lt;?xml&quot; ) &gt;= 0 ): continue<br></td></tr
><tr
id=sl_svn11_70

><td class="source">                    # add line<br></td></tr
><tr
id=sl_svn11_71

><td class="source">                    if sys.version &lt; &#39;3&#39;:<br></td></tr
><tr
id=sl_svn11_72

><td class="source">                        addon_xml += unicode( line.rstrip() + &quot;\n&quot;, &quot;UTF-8&quot; )<br></td></tr
><tr
id=sl_svn11_73

><td class="source">                    else:<br></td></tr
><tr
id=sl_svn11_74

><td class="source">                        addon_xml += line.rstrip() + &quot;\n&quot;<br></td></tr
><tr
id=sl_svn11_75

><td class="source">                # we succeeded so add to our final addons.xml text<br></td></tr
><tr
id=sl_svn11_76

><td class="source">                addons_xml += addon_xml.rstrip() + &quot;\n\n&quot;<br></td></tr
><tr
id=sl_svn11_77

><td class="source">            except Exception as e:<br></td></tr
><tr
id=sl_svn11_78

><td class="source">                # missing or poorly formatted addon.xml<br></td></tr
><tr
id=sl_svn11_79

><td class="source">                print(&quot;Excluding %s for %s&quot; % ( _path, e ))<br></td></tr
><tr
id=sl_svn11_80

><td class="source">        # clean and add closing tag<br></td></tr
><tr
id=sl_svn11_81

><td class="source">        addons_xml = addons_xml.strip() + u(&quot;\n&lt;/addons&gt;\n&quot;)<br></td></tr
><tr
id=sl_svn11_82

><td class="source">        # save file<br></td></tr
><tr
id=sl_svn11_83

><td class="source">        self._save_file( addons_xml.encode( &quot;UTF-8&quot; ), file=&quot;addons.xml&quot; )<br></td></tr
><tr
id=sl_svn11_84

><td class="source"> <br></td></tr
><tr
id=sl_svn11_85

><td class="source">    def _generate_md5_file( self ):<br></td></tr
><tr
id=sl_svn11_86

><td class="source">        # create a new md5 hash<br></td></tr
><tr
id=sl_svn11_87

><td class="source">        try:<br></td></tr
><tr
id=sl_svn11_88

><td class="source">            import md5<br></td></tr
><tr
id=sl_svn11_89

><td class="source">            m = md5.new( open( &quot;addons.xml&quot;, &quot;r&quot; ).read() ).hexdigest()<br></td></tr
><tr
id=sl_svn11_90

><td class="source">        except ImportError:<br></td></tr
><tr
id=sl_svn11_91

><td class="source">            import hashlib<br></td></tr
><tr
id=sl_svn11_92

><td class="source">            m = hashlib.md5( open( &quot;addons.xml&quot;, &quot;r&quot;, encoding=&quot;UTF-8&quot; ).read().encode( &quot;UTF-8&quot; ) ).hexdigest()<br></td></tr
><tr
id=sl_svn11_93

><td class="source"> <br></td></tr
><tr
id=sl_svn11_94

><td class="source">        # save file<br></td></tr
><tr
id=sl_svn11_95

><td class="source">        try:<br></td></tr
><tr
id=sl_svn11_96

><td class="source">            self._save_file( m.encode( &quot;UTF-8&quot; ), file=&quot;addons.xml.md5&quot; )<br></td></tr
><tr
id=sl_svn11_97

><td class="source">        except Exception as e:<br></td></tr
><tr
id=sl_svn11_98

><td class="source">            # oops<br></td></tr
><tr
id=sl_svn11_99

><td class="source">            print(&quot;An error occurred creating addons.xml.md5 file!\n%s&quot; % e)<br></td></tr
><tr
id=sl_svn11_100

><td class="source"> <br></td></tr
><tr
id=sl_svn11_101

><td class="source">    def _save_file( self, data, file ):<br></td></tr
><tr
id=sl_svn11_102

><td class="source">        try:<br></td></tr
><tr
id=sl_svn11_103

><td class="source">            # write data to the file (use b for Python 3)<br></td></tr
><tr
id=sl_svn11_104

><td class="source">            open( file, &quot;wb&quot; ).write( data )<br></td></tr
><tr
id=sl_svn11_105

><td class="source">        except Exception as e:<br></td></tr
><tr
id=sl_svn11_106

><td class="source">            # oops<br></td></tr
><tr
id=sl_svn11_107

><td class="source">            print(&quot;An error occurred saving %s file!\n%s&quot; % ( file, e ))<br></td></tr
><tr
id=sl_svn11_108

><td class="source"> <br></td></tr
><tr
id=sl_svn11_109

><td class="source"> <br></td></tr
><tr
id=sl_svn11_110

><td class="source">if ( __name__ == &quot;__main__&quot; ):<br></td></tr
><tr
id=sl_svn11_111

><td class="source">    # start<br></td></tr
><tr
id=sl_svn11_112

><td class="source">    Generator()<br></td></tr
></table></pre>
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
</td>
</tr></table>

 
<script type="text/javascript">
 var lineNumUnderMouse = -1;
 
 function gutterOver(num) {
 gutterOut();
 var newTR = document.getElementById('gr_svn11_' + num);
 if (newTR) {
 newTR.className = 'undermouse';
 }
 lineNumUnderMouse = num;
 }
 function gutterOut() {
 if (lineNumUnderMouse != -1) {
 var oldTR = document.getElementById(
 'gr_svn11_' + lineNumUnderMouse);
 if (oldTR) {
 oldTR.className = '';
 }
 lineNumUnderMouse = -1;
 }
 }
 var numsGenState = {table_base_id: 'nums_table_'};
 var srcGenState = {table_base_id: 'src_table_'};
 var alignerRunning = false;
 var startOver = false;
 function setLineNumberHeights() {
 if (alignerRunning) {
 startOver = true;
 return;
 }
 numsGenState.chunk_id = 0;
 numsGenState.table = document.getElementById('nums_table_0');
 numsGenState.row_num = 0;
 if (!numsGenState.table) {
 return; // Silently exit if no file is present.
 }
 srcGenState.chunk_id = 0;
 srcGenState.table = document.getElementById('src_table_0');
 srcGenState.row_num = 0;
 alignerRunning = true;
 continueToSetLineNumberHeights();
 }
 function rowGenerator(genState) {
 if (genState.row_num < genState.table.rows.length) {
 var currentRow = genState.table.rows[genState.row_num];
 genState.row_num++;
 return currentRow;
 }
 var newTable = document.getElementById(
 genState.table_base_id + (genState.chunk_id + 1));
 if (newTable) {
 genState.chunk_id++;
 genState.row_num = 0;
 genState.table = newTable;
 return genState.table.rows[0];
 }
 return null;
 }
 var MAX_ROWS_PER_PASS = 1000;
 function continueToSetLineNumberHeights() {
 var rowsInThisPass = 0;
 var numRow = 1;
 var srcRow = 1;
 while (numRow && srcRow && rowsInThisPass < MAX_ROWS_PER_PASS) {
 numRow = rowGenerator(numsGenState);
 srcRow = rowGenerator(srcGenState);
 rowsInThisPass++;
 if (numRow && srcRow) {
 if (numRow.offsetHeight != srcRow.offsetHeight) {
 numRow.firstChild.style.height = srcRow.offsetHeight + 'px';
 }
 }
 }
 if (rowsInThisPass >= MAX_ROWS_PER_PASS) {
 setTimeout(continueToSetLineNumberHeights, 10);
 } else {
 alignerRunning = false;
 if (startOver) {
 startOver = false;
 setTimeout(setLineNumberHeights, 500);
 }
 }
 }
 function initLineNumberHeights() {
 // Do 2 complete passes, because there can be races
 // between this code and prettify.
 startOver = true;
 setTimeout(setLineNumberHeights, 250);
 window.onresize = setLineNumberHeights;
 }
 initLineNumberHeights();
</script>

 
 
 <div id="log">
 <div style="text-align:right">
 <a class="ifCollapse" href="#" onclick="_toggleMeta(this); return false">Show details</a>
 <a class="ifExpand" href="#" onclick="_toggleMeta(this); return false">Hide details</a>
 </div>
 <div class="ifExpand">
 
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="changelog">
 <p>Change log</p>
 <div>
 <a href="/p/repository-xbmcmania/source/detail?spec=svn11&amp;r=1">r1</a>
 by rafael.miguel
 on Mar 25, 2015
 &nbsp; <a href="/p/repository-xbmcmania/source/diff?spec=svn11&r=1&amp;format=side&amp;path=/trunk/Helix/addons_xml_generator.py&amp;old_path=/trunk/Helix/addons_xml_generator.py&amp;old=">Diff</a>
 </div>
 <pre>Reset</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/repository-xbmcmania/source/detail?r=1&spec=svn11';
 var publish_url = '/p/repository-xbmcmania/source/detail?r=1&spec=svn11#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/trunk');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/README.md');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/README.md?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/addons.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/addons.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/addons.xml.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/addons.xml.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/addons_xml_generator.py');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/addons_xml_generator.py?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/plugin.program.executor');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/plugin.program.executor?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/plugin.program.executor/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/plugin.program.executor/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/plugin.program.executor/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/plugin.program.executor/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/plugin.program.executor/plugin.program.executor-0.2.6.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/plugin.program.executor/plugin.program.executor-0.2.6.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/plugin.program.executor/plugin.program.executor-0.2.6.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/plugin.program.executor/plugin.program.executor-0.2.6.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.androidarm');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.androidarm?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.androidarm/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.androidarm/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.androidarm/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.androidarm/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.androidarm/pvr.iptvImagenio.androidarm-1.0.42.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.androidarm/pvr.iptvImagenio.androidarm-1.0.42.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.linux');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.linux?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.linux/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.linux/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.linux/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.linux/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.linux/pvr.iptvImagenio.linux-1.0.42.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.linux/pvr.iptvImagenio.linux-1.0.42.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.mac');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.mac?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.mac/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.mac/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.mac/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.mac/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.mac/pvr.iptvImagenio.mac-1.0.42.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.mac/pvr.iptvImagenio.mac-1.0.42.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.open');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.open/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.open/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.open/pvr.iptvImagenio.open-1.0.42.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open/pvr.iptvImagenio.open-1.0.42.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.open32');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open32?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.open32/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open32/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.open32/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open32/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.open32/pvr.iptvImagenio.open32-1.0.42.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open32/pvr.iptvImagenio.open32-1.0.42.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.rpi');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.rpi?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.rpi/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.rpi/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.rpi/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.rpi/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.rpi/pvr.iptvImagenio.rpi-1.0.42.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.rpi/pvr.iptvImagenio.rpi-1.0.42.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.win');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.win?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.win/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.win/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.win/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.win/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/pvr.iptvImagenio.win/pvr.iptvImagenio.win-1.0.42.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.win/pvr.iptvImagenio.win-1.0.42.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/repository.xbmcmania.gotham');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/repository.xbmcmania.gotham.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/repository.xbmcmania.gotham/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/repository.xbmcmania.gotham/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/repository.xbmcmania.gotham/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/repository.xbmcmania.gotham/repository.xbmcmania.gotham-1.0.1.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham/repository.xbmcmania.gotham-1.0.1.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/repository.xbmcmania.gotham/repository.xbmcmania.gotham-1.0.1.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham/repository.xbmcmania.gotham-1.0.1.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artistslideshow');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artistslideshow?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artistslideshow/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artistslideshow/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artistslideshow/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artistslideshow/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artistslideshow/script.artistslideshow-1.7.0.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artistslideshow/script.artistslideshow-1.7.0.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artistslideshow/script.artistslideshow-1.7.0.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artistslideshow/script.artistslideshow-1.7.0.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artwork.downloader');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artwork.downloader/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artwork.downloader/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artwork.downloader/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artwork.downloader/fanart.jpg');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/fanart.jpg?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artwork.downloader/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artwork.downloader/readme.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/readme.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artwork.downloader/script.artwork.downloader-12.0.29.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/script.artwork.downloader-12.0.29.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.artwork.downloader/script.artwork.downloader-12.0.29.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/script.artwork.downloader-12.0.29.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cdartmanager');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cdartmanager?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cdartmanager/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cdartmanager/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cdartmanager/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cdartmanager/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cdartmanager/script.cdartmanager-4.0.5.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cdartmanager/script.cdartmanager-4.0.5.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cdartmanager/script.cdartmanager-4.0.5.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cdartmanager/script.cdartmanager-4.0.5.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cinema.experience');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cinema.experience/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cinema.experience/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cinema.experience/fanart.jpg');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/fanart.jpg?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cinema.experience/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cinema.experience/script.cinema.experience-4.0.13.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/script.cinema.experience-4.0.13.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cinema.experience/script.cinema.experience-4.0.13.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/script.cinema.experience-4.0.13.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.color.picker');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.color.picker?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.color.picker/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.color.picker/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.color.picker/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.color.picker/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.color.picker/script.color.picker-1.0.7.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.color.picker/script.color.picker-1.0.7.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.color.picker/script.color.picker-1.0.7.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.color.picker/script.color.picker-1.0.7.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.common.plugin.cache');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.common.plugin.cache/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.common.plugin.cache/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.common.plugin.cache/icon and thumbnail licensing.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/icon and thumbnail licensing.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.common.plugin.cache/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.common.plugin.cache/script.common.plugin.cache-2.5.5.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/script.common.plugin.cache-2.5.5.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.common.plugin.cache/script.common.plugin.cache-2.5.5.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/script.common.plugin.cache-2.5.5.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cu.lrclyrics');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cu.lrclyrics?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cu.lrclyrics/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cu.lrclyrics/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cu.lrclyrics/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cu.lrclyrics/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cu.lrclyrics/script.cu.lrclyrics-2.0.12.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cu.lrclyrics/script.cu.lrclyrics-2.0.12.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.cu.lrclyrics/script.cu.lrclyrics-2.0.12.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cu.lrclyrics/script.cu.lrclyrics-2.0.12.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.favourites');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.favourites/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.favourites/README.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/README.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.favourites/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.favourites/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.favourites/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.favourites/script.favourites-6.0.1.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/script.favourites-6.0.1.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.favourites/script.favourites-6.0.1.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/script.favourites-6.0.1.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.globalsearch');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.globalsearch/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.globalsearch/README.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/README.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.globalsearch/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.globalsearch/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.globalsearch/fanart.jpg');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/fanart.jpg?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.globalsearch/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.globalsearch/script.globalsearch-3.0.4.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/script.globalsearch-3.0.4.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.globalsearch/script.globalsearch-3.0.4.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/script.globalsearch-3.0.4.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.metadata.actors');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.metadata.actors?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.metadata.actors/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.metadata.actors/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.metadata.actors/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.metadata.actors/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.metadata.actors/script.metadata.actors-0.9.8.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.metadata.actors/script.metadata.actors-0.9.8.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.metadata.actors/script.metadata.actors-0.9.8.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.metadata.actors/script.metadata.actors-0.9.8.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.beautifulsoup4');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.beautifulsoup4/AUTHORS.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/AUTHORS.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.beautifulsoup4/COPYING.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/COPYING.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.beautifulsoup4/LICENSE');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/LICENSE?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.beautifulsoup4/README.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/README.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.beautifulsoup4/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.beautifulsoup4/script.module.beautifulsoup4-4.3.2.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/script.module.beautifulsoup4-4.3.2.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.beautifulsoup4/script.module.beautifulsoup4-4.3.2.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/script.module.beautifulsoup4-4.3.2.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.chardet');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.chardet/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.chardet/README.md');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/README.md?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.chardet/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.chardet/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.chardet/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.chardet/script.module.chardet-2.2.1.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/script.module.chardet-2.2.1.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.chardet/script.module.chardet-2.2.1.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/script.module.chardet-2.2.1.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.myconnpy');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.myconnpy/COPYING');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/COPYING?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.myconnpy/ChangeLog');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/ChangeLog?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.myconnpy/EXCEPTIONS-CLIENT');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/EXCEPTIONS-CLIENT?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.myconnpy/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.myconnpy/PKG-INFO');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/PKG-INFO?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.myconnpy/README');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/README?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.myconnpy/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.myconnpy/script.module.myconnpy-1.1.7.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/script.module.myconnpy-1.1.7.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.myconnpy/script.module.myconnpy-1.1.7.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/script.module.myconnpy-1.1.7.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.requests');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.requests/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.requests/README.md');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/README.md?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.requests/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.requests/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.requests/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.requests/script.module.requests-2.4.3.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/script.module.requests-2.4.3.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.requests/script.module.requests-2.4.3.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/script.module.requests-2.4.3.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.simplejson');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.simplejson/CHANGELOG.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson/CHANGELOG.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.simplejson/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.simplejson/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.simplejson/script.module.simplejson-3.3.0.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson/script.module.simplejson-3.3.0.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.module.simplejson/script.module.simplejson-3.3.0.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson/script.module.simplejson-3.3.0.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moreinfo');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moreinfo/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moreinfo/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moreinfo/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moreinfo/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moreinfo/script.moreinfo-0.0.2.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/script.moreinfo-0.0.2.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moreinfo/script.moreinfo-0.0.2.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/script.moreinfo-0.0.2.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moviesetart');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moviesetart?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moviesetart/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moviesetart/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moviesetart/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moviesetart/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moviesetart/script.moviesetart-0.2.2.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moviesetart/script.moviesetart-0.2.2.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.moviesetart/script.moviesetart-0.2.2.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moviesetart/script.moviesetart-0.2.2.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.nox.coloricon.downloader');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.nox.coloricon.downloader/.gitattributes');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/.gitattributes?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.nox.coloricon.downloader/.gitignore');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/.gitignore?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.nox.coloricon.downloader/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.nox.coloricon.downloader/README.md');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/README.md?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.nox.coloricon.downloader/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.nox.coloricon.downloader/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.nox.coloricon.downloader/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.nox.coloricon.downloader/script.nox.coloricon.downloader-0.0.1.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/script.nox.coloricon.downloader-0.0.1.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.nox.coloricon.downloader/script.nox.coloricon.downloader-0.0.1.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/script.nox.coloricon.downloader-0.0.1.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playalbum');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playalbum/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playalbum/README.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/README.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playalbum/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playalbum/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playalbum/icon.png');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/icon.png?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playalbum/script.playalbum-2.0.1.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/script.playalbum-2.0.1.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playalbum/script.playalbum-2.0.1.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/script.playalbum-2.0.1.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playlists');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playlists/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playlists/README.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/README.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playlists/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playlists/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playlists/script.playlists-2.0.1.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/script.playlists-2.0.1.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.playlists/script.playlists-2.0.1.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/script.playlists-2.0.1.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randomandlastitems');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randomandlastitems/LICENSE.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/LICENSE.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randomandlastitems/README.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/README.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randomandlastitems/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randomandlastitems/changelog.txt');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/changelog.txt?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randomandlastitems/script.randomandlastitems-2.2.2.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/script.randomandlastitems-2.2.2.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randomandlastitems/script.randomandlastitems-2.2.2.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/script.randomandlastitems-2.2.2.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randommovie');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randommovie?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randommovie/addon.xml');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randommovie/addon.xml?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randommovie/script.randommovie-0.1.1.zip');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randommovie/script.randommovie-0.1.1.zip?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.randommovie/script.randommovie-0.1.1.zip.md5');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randommovie/script.randommovie-0.1.1.zip.md5?r\x3d1\x26spec\x3dsvn11');
 
 
 changed_paths.push('/trunk/Gotham/script.ratingupdate');
 changed_urls.push('/p/repository-xbmcmania/source/browse/trunk/Gotham/script.ratingupdate?r\x3d1\x26spec\x3dsvn11');
 
 
 function getCurrentPageIndex() {
 for (var i = 0; i < changed_paths.length; i++) {
 if (selected_path == changed_paths[i]) {
 return i;
 }
 }
 }
 function getNextPage() {
 var i = getCurrentPageIndex();
 if (i < changed_paths.length - 1) {
 return changed_urls[i + 1];
 }
 return null;
 }
 function getPreviousPage() {
 var i = getCurrentPageIndex();
 if (i > 0) {
 return changed_urls[i - 1];
 }
 return null;
 }
 function gotoNextPage() {
 var page = getNextPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoPreviousPage() {
 var page = getPreviousPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoDetailPage() {
 window.location = detail_url;
 }
 function gotoPublishPage() {
 window.location = publish_url;
 }
</script>

 
 <style type="text/css">
 #review_nav {
 border-top: 3px solid white;
 padding-top: 6px;
 margin-top: 1em;
 }
 #review_nav td {
 vertical-align: middle;
 }
 #review_nav select {
 margin: .5em 0;
 }
 </style>
 <div id="review_nav">
 <table><tr><td>Go to:&nbsp;</td><td>
 <select name="files_in_rev" onchange="window.location=this.value">
 
 <option value="/p/repository-xbmcmania/source/browse/trunk?r=1&amp;spec=svn11"
 
 >/trunk</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham?r=1&amp;spec=svn11"
 
 >/trunk/Gotham</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/README.md?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/README.md</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/addons.xml?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/addons.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/addons.xml.md5?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/addons.xml.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/addons_xml_generator.py?r=1&amp;spec=svn11"
 
 >...k/Gotham/addons_xml_generator.py</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/plugin.program.executor?r=1&amp;spec=svn11"
 
 >...k/Gotham/plugin.program.executor</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/plugin.program.executor/addon.xml?r=1&amp;spec=svn11"
 
 >...lugin.program.executor/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/plugin.program.executor/icon.png?r=1&amp;spec=svn11"
 
 >...plugin.program.executor/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/plugin.program.executor/plugin.program.executor-0.2.6.zip?r=1&amp;spec=svn11"
 
 >...lugin.program.executor-0.2.6.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/plugin.program.executor/plugin.program.executor-0.2.6.zip.md5?r=1&amp;spec=svn11"
 
 >...n.program.executor-0.2.6.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.androidarm?r=1&amp;spec=svn11"
 
 >...tham/pvr.iptvImagenio.androidarm</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.androidarm/addon.xml?r=1&amp;spec=svn11"
 
 >...ptvImagenio.androidarm/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.androidarm/icon.png?r=1&amp;spec=svn11"
 
 >...iptvImagenio.androidarm/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.androidarm/pvr.iptvImagenio.androidarm-1.0.42.zip?r=1&amp;spec=svn11"
 
 >...tvImagenio.androidarm-1.0.42.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.linux?r=1&amp;spec=svn11"
 
 >...nk/Gotham/pvr.iptvImagenio.linux</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.linux/addon.xml?r=1&amp;spec=svn11"
 
 >...pvr.iptvImagenio.linux/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.linux/icon.png?r=1&amp;spec=svn11"
 
 >.../pvr.iptvImagenio.linux/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.linux/pvr.iptvImagenio.linux-1.0.42.zip?r=1&amp;spec=svn11"
 
 >...vr.iptvImagenio.linux-1.0.42.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.mac?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/pvr.iptvImagenio.mac</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.mac/addon.xml?r=1&amp;spec=svn11"
 
 >...m/pvr.iptvImagenio.mac/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.mac/icon.png?r=1&amp;spec=svn11"
 
 >...am/pvr.iptvImagenio.mac/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.mac/pvr.iptvImagenio.mac-1.0.42.zip?r=1&amp;spec=svn11"
 
 >.../pvr.iptvImagenio.mac-1.0.42.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/pvr.iptvImagenio.open</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open/addon.xml?r=1&amp;spec=svn11"
 
 >.../pvr.iptvImagenio.open/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open/icon.png?r=1&amp;spec=svn11"
 
 >...m/pvr.iptvImagenio.open/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open/pvr.iptvImagenio.open-1.0.42.zip?r=1&amp;spec=svn11"
 
 >...pvr.iptvImagenio.open-1.0.42.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open32?r=1&amp;spec=svn11"
 
 >...k/Gotham/pvr.iptvImagenio.open32</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open32/addon.xml?r=1&amp;spec=svn11"
 
 >...vr.iptvImagenio.open32/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open32/icon.png?r=1&amp;spec=svn11"
 
 >...pvr.iptvImagenio.open32/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.open32/pvr.iptvImagenio.open32-1.0.42.zip?r=1&amp;spec=svn11"
 
 >...r.iptvImagenio.open32-1.0.42.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.rpi?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/pvr.iptvImagenio.rpi</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.rpi/addon.xml?r=1&amp;spec=svn11"
 
 >...m/pvr.iptvImagenio.rpi/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.rpi/icon.png?r=1&amp;spec=svn11"
 
 >...am/pvr.iptvImagenio.rpi/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.rpi/pvr.iptvImagenio.rpi-1.0.42.zip?r=1&amp;spec=svn11"
 
 >.../pvr.iptvImagenio.rpi-1.0.42.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.win?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/pvr.iptvImagenio.win</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.win/addon.xml?r=1&amp;spec=svn11"
 
 >...m/pvr.iptvImagenio.win/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.win/icon.png?r=1&amp;spec=svn11"
 
 >...am/pvr.iptvImagenio.win/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/pvr.iptvImagenio.win/pvr.iptvImagenio.win-1.0.42.zip?r=1&amp;spec=svn11"
 
 >.../pvr.iptvImagenio.win-1.0.42.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham?r=1&amp;spec=svn11"
 
 >...tham/repository.xbmcmania.gotham</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham.zip?r=1&amp;spec=svn11"
 
 >.../repository.xbmcmania.gotham.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham/addon.xml?r=1&amp;spec=svn11"
 
 >...itory.xbmcmania.gotham/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham/changelog.txt?r=1&amp;spec=svn11"
 
 >...y.xbmcmania.gotham/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham/icon.png?r=1&amp;spec=svn11"
 
 >...sitory.xbmcmania.gotham/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham/repository.xbmcmania.gotham-1.0.1.zip?r=1&amp;spec=svn11"
 
 >...itory.xbmcmania.gotham-1.0.1.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/repository.xbmcmania.gotham/repository.xbmcmania.gotham-1.0.1.zip.md5?r=1&amp;spec=svn11"
 
 >...y.xbmcmania.gotham-1.0.1.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artistslideshow?r=1&amp;spec=svn11"
 
 >...nk/Gotham/script.artistslideshow</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artistslideshow/addon.xml?r=1&amp;spec=svn11"
 
 >...script.artistslideshow/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artistslideshow/icon.png?r=1&amp;spec=svn11"
 
 >.../script.artistslideshow/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artistslideshow/script.artistslideshow-1.7.0.zip?r=1&amp;spec=svn11"
 
 >...script.artistslideshow-1.7.0.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artistslideshow/script.artistslideshow-1.7.0.zip.md5?r=1&amp;spec=svn11"
 
 >...pt.artistslideshow-1.7.0.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader?r=1&amp;spec=svn11"
 
 >...Gotham/script.artwork.downloader</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...t.artwork.downloader/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/addon.xml?r=1&amp;spec=svn11"
 
 >...ipt.artwork.downloader/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/changelog.txt?r=1&amp;spec=svn11"
 
 >...artwork.downloader/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/fanart.jpg?r=1&amp;spec=svn11"
 
 >...pt.artwork.downloader/fanart.jpg</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/icon.png?r=1&amp;spec=svn11"
 
 >...ript.artwork.downloader/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/readme.txt?r=1&amp;spec=svn11"
 
 >...pt.artwork.downloader/readme.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/script.artwork.downloader-12.0.29.zip?r=1&amp;spec=svn11"
 
 >...t.artwork.downloader-12.0.29.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.artwork.downloader/script.artwork.downloader-12.0.29.zip.md5?r=1&amp;spec=svn11"
 
 >...twork.downloader-12.0.29.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cdartmanager?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.cdartmanager</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cdartmanager/addon.xml?r=1&amp;spec=svn11"
 
 >...am/script.cdartmanager/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cdartmanager/icon.png?r=1&amp;spec=svn11"
 
 >...ham/script.cdartmanager/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cdartmanager/script.cdartmanager-4.0.5.zip?r=1&amp;spec=svn11"
 
 >...er/script.cdartmanager-4.0.5.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cdartmanager/script.cdartmanager-4.0.5.zip.md5?r=1&amp;spec=svn11"
 
 >...cript.cdartmanager-4.0.5.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience?r=1&amp;spec=svn11"
 
 >.../Gotham/script.cinema.experience</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/addon.xml?r=1&amp;spec=svn11"
 
 >...ript.cinema.experience/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/changelog.txt?r=1&amp;spec=svn11"
 
 >....cinema.experience/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/fanart.jpg?r=1&amp;spec=svn11"
 
 >...ipt.cinema.experience/fanart.jpg</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/icon.png?r=1&amp;spec=svn11"
 
 >...cript.cinema.experience/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/script.cinema.experience-4.0.13.zip?r=1&amp;spec=svn11"
 
 >...ipt.cinema.experience-4.0.13.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cinema.experience/script.cinema.experience-4.0.13.zip.md5?r=1&amp;spec=svn11"
 
 >...cinema.experience-4.0.13.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.color.picker?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.color.picker</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.color.picker/addon.xml?r=1&amp;spec=svn11"
 
 >...am/script.color.picker/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.color.picker/icon.png?r=1&amp;spec=svn11"
 
 >...ham/script.color.picker/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.color.picker/script.color.picker-1.0.7.zip?r=1&amp;spec=svn11"
 
 >...er/script.color.picker-1.0.7.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.color.picker/script.color.picker-1.0.7.zip.md5?r=1&amp;spec=svn11"
 
 >...cript.color.picker-1.0.7.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache?r=1&amp;spec=svn11"
 
 >...otham/script.common.plugin.cache</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/addon.xml?r=1&amp;spec=svn11"
 
 >...pt.common.plugin.cache/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/changelog.txt?r=1&amp;spec=svn11"
 
 >...ommon.plugin.cache/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/icon and thumbnail licensing.txt?r=1&amp;spec=svn11"
 
 >...icon and thumbnail licensing.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/icon.png?r=1&amp;spec=svn11"
 
 >...ipt.common.plugin.cache/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/script.common.plugin.cache-2.5.5.zip?r=1&amp;spec=svn11"
 
 >...pt.common.plugin.cache-2.5.5.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.common.plugin.cache/script.common.plugin.cache-2.5.5.zip.md5?r=1&amp;spec=svn11"
 
 >...ommon.plugin.cache-2.5.5.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cu.lrclyrics?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.cu.lrclyrics</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cu.lrclyrics/addon.xml?r=1&amp;spec=svn11"
 
 >...am/script.cu.lrclyrics/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cu.lrclyrics/icon.png?r=1&amp;spec=svn11"
 
 >...ham/script.cu.lrclyrics/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cu.lrclyrics/script.cu.lrclyrics-2.0.12.zip?r=1&amp;spec=svn11"
 
 >...s/script.cu.lrclyrics-2.0.12.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.cu.lrclyrics/script.cu.lrclyrics-2.0.12.zip.md5?r=1&amp;spec=svn11"
 
 >...ript.cu.lrclyrics-2.0.12.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.favourites</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...am/script.favourites/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/README.txt?r=1&amp;spec=svn11"
 
 >...ham/script.favourites/README.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/addon.xml?r=1&amp;spec=svn11"
 
 >...tham/script.favourites/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/changelog.txt?r=1&amp;spec=svn11"
 
 >.../script.favourites/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/icon.png?r=1&amp;spec=svn11"
 
 >...otham/script.favourites/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/script.favourites-6.0.1.zip?r=1&amp;spec=svn11"
 
 >...ites/script.favourites-6.0.1.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.favourites/script.favourites-6.0.1.zip.md5?r=1&amp;spec=svn11"
 
 >.../script.favourites-6.0.1.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.globalsearch</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/LICENSE.txt?r=1&amp;spec=svn11"
 
 >.../script.globalsearch/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/README.txt?r=1&amp;spec=svn11"
 
 >...m/script.globalsearch/README.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/addon.xml?r=1&amp;spec=svn11"
 
 >...am/script.globalsearch/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/changelog.txt?r=1&amp;spec=svn11"
 
 >...cript.globalsearch/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/fanart.jpg?r=1&amp;spec=svn11"
 
 >...m/script.globalsearch/fanart.jpg</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/icon.png?r=1&amp;spec=svn11"
 
 >...ham/script.globalsearch/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/script.globalsearch-3.0.4.md5?r=1&amp;spec=svn11"
 
 >...ch/script.globalsearch-3.0.4.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.globalsearch/script.globalsearch-3.0.4.zip?r=1&amp;spec=svn11"
 
 >...ch/script.globalsearch-3.0.4.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.metadata.actors?r=1&amp;spec=svn11"
 
 >...nk/Gotham/script.metadata.actors</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.metadata.actors/addon.xml?r=1&amp;spec=svn11"
 
 >...script.metadata.actors/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.metadata.actors/icon.png?r=1&amp;spec=svn11"
 
 >.../script.metadata.actors/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.metadata.actors/script.metadata.actors-0.9.8.zip?r=1&amp;spec=svn11"
 
 >...script.metadata.actors-0.9.8.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.metadata.actors/script.metadata.actors-0.9.8.zip.md5?r=1&amp;spec=svn11"
 
 >...pt.metadata.actors-0.9.8.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4?r=1&amp;spec=svn11"
 
 >...ham/script.module.beautifulsoup4</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/AUTHORS.txt?r=1&amp;spec=svn11"
 
 >...odule.beautifulsoup4/AUTHORS.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/COPYING.txt?r=1&amp;spec=svn11"
 
 >...odule.beautifulsoup4/COPYING.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/LICENSE?r=1&amp;spec=svn11"
 
 >...pt.module.beautifulsoup4/LICENSE</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/README.txt?r=1&amp;spec=svn11"
 
 >...module.beautifulsoup4/README.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/addon.xml?r=1&amp;spec=svn11"
 
 >....module.beautifulsoup4/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/script.module.beautifulsoup4-4.3.2.zip?r=1&amp;spec=svn11"
 
 >....module.beautifulsoup4-4.3.2.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.beautifulsoup4/script.module.beautifulsoup4-4.3.2.zip.md5?r=1&amp;spec=svn11"
 
 >...ule.beautifulsoup4-4.3.2.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.module.chardet</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...cript.module.chardet/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/README.md?r=1&amp;spec=svn11"
 
 >.../script.module.chardet/README.md</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/addon.xml?r=1&amp;spec=svn11"
 
 >.../script.module.chardet/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/changelog.txt?r=1&amp;spec=svn11"
 
 >...ipt.module.chardet/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/icon.png?r=1&amp;spec=svn11"
 
 >...m/script.module.chardet/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/script.module.chardet-2.2.1.zip?r=1&amp;spec=svn11"
 
 >.../script.module.chardet-2.2.1.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.chardet/script.module.chardet-2.2.1.zip.md5?r=1&amp;spec=svn11"
 
 >...ipt.module.chardet-2.2.1.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy?r=1&amp;spec=svn11"
 
 >...nk/Gotham/script.module.myconnpy</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/COPYING?r=1&amp;spec=svn11"
 
 >...m/script.module.myconnpy/COPYING</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/ChangeLog?r=1&amp;spec=svn11"
 
 >...script.module.myconnpy/ChangeLog</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/EXCEPTIONS-CLIENT?r=1&amp;spec=svn11"
 
 >...odule.myconnpy/EXCEPTIONS-CLIENT</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...ript.module.myconnpy/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/PKG-INFO?r=1&amp;spec=svn11"
 
 >.../script.module.myconnpy/PKG-INFO</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/README?r=1&amp;spec=svn11"
 
 >...am/script.module.myconnpy/README</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/addon.xml?r=1&amp;spec=svn11"
 
 >...script.module.myconnpy/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/script.module.myconnpy-1.1.7.zip?r=1&amp;spec=svn11"
 
 >...script.module.myconnpy-1.1.7.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.myconnpy/script.module.myconnpy-1.1.7.zip.md5?r=1&amp;spec=svn11"
 
 >...pt.module.myconnpy-1.1.7.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests?r=1&amp;spec=svn11"
 
 >...nk/Gotham/script.module.requests</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...ript.module.requests/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/README.md?r=1&amp;spec=svn11"
 
 >...script.module.requests/README.md</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/addon.xml?r=1&amp;spec=svn11"
 
 >...script.module.requests/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/changelog.txt?r=1&amp;spec=svn11"
 
 >...pt.module.requests/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/icon.png?r=1&amp;spec=svn11"
 
 >.../script.module.requests/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/script.module.requests-2.4.3.zip?r=1&amp;spec=svn11"
 
 >...script.module.requests-2.4.3.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.requests/script.module.requests-2.4.3.zip.md5?r=1&amp;spec=svn11"
 
 >...pt.module.requests-2.4.3.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson?r=1&amp;spec=svn11"
 
 >.../Gotham/script.module.simplejson</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson/CHANGELOG.txt?r=1&amp;spec=svn11"
 
 >....module.simplejson/CHANGELOG.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...pt.module.simplejson/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson/addon.xml?r=1&amp;spec=svn11"
 
 >...ript.module.simplejson/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson/script.module.simplejson-3.3.0.zip?r=1&amp;spec=svn11"
 
 >...ript.module.simplejson-3.3.0.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.module.simplejson/script.module.simplejson-3.3.0.zip.md5?r=1&amp;spec=svn11"
 
 >....module.simplejson-3.3.0.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.moreinfo</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...tham/script.moreinfo/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/addon.xml?r=1&amp;spec=svn11"
 
 >...Gotham/script.moreinfo/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/changelog.txt?r=1&amp;spec=svn11"
 
 >...am/script.moreinfo/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/icon.png?r=1&amp;spec=svn11"
 
 >.../Gotham/script.moreinfo/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/script.moreinfo-0.0.2.zip?r=1&amp;spec=svn11"
 
 >...reinfo/script.moreinfo-0.0.2.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moreinfo/script.moreinfo-0.0.2.zip.md5?r=1&amp;spec=svn11"
 
 >...fo/script.moreinfo-0.0.2.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moviesetart?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.moviesetart</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moviesetart/addon.xml?r=1&amp;spec=svn11"
 
 >...ham/script.moviesetart/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moviesetart/icon.png?r=1&amp;spec=svn11"
 
 >...tham/script.moviesetart/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moviesetart/script.moviesetart-0.2.2.zip?r=1&amp;spec=svn11"
 
 >...art/script.moviesetart-0.2.2.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.moviesetart/script.moviesetart-0.2.2.zip.md5?r=1&amp;spec=svn11"
 
 >...script.moviesetart-0.2.2.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader?r=1&amp;spec=svn11"
 
 >.../script.nox.coloricon.downloader</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/.gitattributes?r=1&amp;spec=svn11"
 
 >...oricon.downloader/.gitattributes</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/.gitignore?r=1&amp;spec=svn11"
 
 >....coloricon.downloader/.gitignore</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...coloricon.downloader/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/README.md?r=1&amp;spec=svn11"
 
 >...x.coloricon.downloader/README.md</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/addon.xml?r=1&amp;spec=svn11"
 
 >...x.coloricon.downloader/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/changelog.txt?r=1&amp;spec=svn11"
 
 >...loricon.downloader/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/icon.png?r=1&amp;spec=svn11"
 
 >...ox.coloricon.downloader/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/script.nox.coloricon.downloader-0.0.1.zip?r=1&amp;spec=svn11"
 
 >...x.coloricon.downloader-0.0.1.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.nox.coloricon.downloader/script.nox.coloricon.downloader-0.0.1.zip.md5?r=1&amp;spec=svn11"
 
 >...loricon.downloader-0.0.1.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.playalbum</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...ham/script.playalbum/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/README.txt?r=1&amp;spec=svn11"
 
 >...tham/script.playalbum/README.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/addon.xml?r=1&amp;spec=svn11"
 
 >...otham/script.playalbum/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/changelog.txt?r=1&amp;spec=svn11"
 
 >...m/script.playalbum/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/icon.png?r=1&amp;spec=svn11"
 
 >...Gotham/script.playalbum/icon.png</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/script.playalbum-2.0.1.zip?r=1&amp;spec=svn11"
 
 >...album/script.playalbum-2.0.1.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playalbum/script.playalbum-2.0.1.zip.md5?r=1&amp;spec=svn11"
 
 >...m/script.playalbum-2.0.1.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.playlists</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...ham/script.playlists/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/README.txt?r=1&amp;spec=svn11"
 
 >...tham/script.playlists/README.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/addon.xml?r=1&amp;spec=svn11"
 
 >...otham/script.playlists/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/changelog.txt?r=1&amp;spec=svn11"
 
 >...m/script.playlists/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/script.playlists-2.0.1.zip?r=1&amp;spec=svn11"
 
 >...lists/script.playlists-2.0.1.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.playlists/script.playlists-2.0.1.zip.md5?r=1&amp;spec=svn11"
 
 >...s/script.playlists-2.0.1.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems?r=1&amp;spec=svn11"
 
 >...Gotham/script.randomandlastitems</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/LICENSE.txt?r=1&amp;spec=svn11"
 
 >...t.randomandlastitems/LICENSE.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/README.txt?r=1&amp;spec=svn11"
 
 >...pt.randomandlastitems/README.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/addon.xml?r=1&amp;spec=svn11"
 
 >...ipt.randomandlastitems/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/changelog.txt?r=1&amp;spec=svn11"
 
 >...randomandlastitems/changelog.txt</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/script.randomandlastitems-2.2.2.zip?r=1&amp;spec=svn11"
 
 >...ipt.randomandlastitems-2.2.2.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randomandlastitems/script.randomandlastitems-2.2.2.zip.md5?r=1&amp;spec=svn11"
 
 >...randomandlastitems-2.2.2.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randommovie?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.randommovie</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randommovie/addon.xml?r=1&amp;spec=svn11"
 
 >...ham/script.randommovie/addon.xml</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randommovie/script.randommovie-0.1.1.zip?r=1&amp;spec=svn11"
 
 >...vie/script.randommovie-0.1.1.zip</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.randommovie/script.randommovie-0.1.1.zip.md5?r=1&amp;spec=svn11"
 
 >...script.randommovie-0.1.1.zip.md5</option>
 
 <option value="/p/repository-xbmcmania/source/browse/trunk/Gotham/script.ratingupdate?r=1&amp;spec=svn11"
 
 >/trunk/Gotham/script.ratingupdate</option>
 
 </select>
 </td></tr></table>
 
 
 



 
 </div>
 
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="older_bubble">
 <p>Older revisions</p>
 
 <a href="/p/repository-xbmcmania/source/list?path=/trunk/Helix/addons_xml_generator.py&start=1">All revisions of this file</a>
 </div>
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="fileinfo_bubble">
 <p>File info</p>
 
 <div>Size: 4370 bytes,
 112 lines</div>
 
 <div><a href="//repository-xbmcmania.googlecode.com/svn/trunk/Helix/addons_xml_generator.py">View raw file</a></div>
 </div>
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 </div>
 </div>


</div>

</div>
</div>

<script src="https://ssl.gstatic.com/codesite/ph/8599073060794244502/js/prettify/prettify.js"></script>
<script type="text/javascript">prettyPrint();</script>


<script src="https://ssl.gstatic.com/codesite/ph/8599073060794244502/js/source_file_scripts.js"></script>

 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/8599073060794244502/js/kibbles.js"></script>
 <script type="text/javascript">
 var lastStop = null;
 var initialized = false;
 
 function updateCursor(next, prev) {
 if (prev && prev.element) {
 prev.element.className = 'cursor_stop cursor_hidden';
 }
 if (next && next.element) {
 next.element.className = 'cursor_stop cursor';
 lastStop = next.index;
 }
 }
 
 function pubRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftDestroyed(data) {
 updateCursorForCell(data.cellId, 'nocursor');
 if (initialized) {
 reloadCursors();
 }
 }
 function reloadCursors() {
 kibbles.skipper.reset();
 loadCursors();
 if (lastStop != null) {
 kibbles.skipper.setCurrentStop(lastStop);
 }
 }
 // possibly the simplest way to insert any newly added comments
 // is to update the class of the corresponding cursor row,
 // then refresh the entire list of rows.
 function updateCursorForCell(cellId, className) {
 var cell = document.getElementById(cellId);
 // we have to go two rows back to find the cursor location
 var row = getPreviousElement(cell.parentNode);
 row.className = className;
 }
 // returns the previous element, ignores text nodes.
 function getPreviousElement(e) {
 var element = e.previousSibling;
 if (element.nodeType == 3) {
 element = element.previousSibling;
 }
 if (element && element.tagName) {
 return element;
 }
 }
 function loadCursors() {
 // register our elements with skipper
 var elements = CR_getElements('*', 'cursor_stop');
 var len = elements.length;
 for (var i = 0; i < len; i++) {
 var element = elements[i]; 
 element.className = 'cursor_stop cursor_hidden';
 kibbles.skipper.append(element);
 }
 }
 function toggleComments() {
 CR_toggleCommentDisplay();
 reloadCursors();
 }
 function keysOnLoadHandler() {
 // setup skipper
 kibbles.skipper.addStopListener(
 kibbles.skipper.LISTENER_TYPE.PRE, updateCursor);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_top', 50);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_bottom', 100);
 // Register our keys
 kibbles.skipper.addFwdKey("n");
 kibbles.skipper.addRevKey("p");
 kibbles.keys.addKeyPressListener(
 'u', function() { window.location = detail_url; });
 kibbles.keys.addKeyPressListener(
 'r', function() { window.location = detail_url + '#publish'; });
 
 kibbles.keys.addKeyPressListener('j', gotoNextPage);
 kibbles.keys.addKeyPressListener('k', gotoPreviousPage);
 
 
 }
 </script>
<script src="https://ssl.gstatic.com/codesite/ph/8599073060794244502/js/code_review_scripts.js"></script>
<script type="text/javascript">
 function showPublishInstructions() {
 var element = document.getElementById('review_instr');
 if (element) {
 element.className = 'opened';
 }
 }
 var codereviews;
 function revsOnLoadHandler() {
 // register our source container with the commenting code
 var paths = {'svn11': '/trunk/Helix/addons_xml_generator.py'}
 codereviews = CR_controller.setup(
 {"domainName": null, "projectHomeUrl": "/p/repository-xbmcmania", "relativeBaseUrl": "", "loggedInUserEmail": "salondigitalpedidos@gmail.com", "assetHostPath": "https://ssl.gstatic.com/codesite/ph", "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/8599073060794244502", "projectName": "repository-xbmcmania", "profileUrl": "/u/107543989748942104600/", "token": "ABZ6GAelVFkqf4ROpDtWudp5VAxYAtD3tg:1434808271687"}, '', 'svn11', paths,
 CR_BrowseIntegrationFactory);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, showPublishInstructions);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_PUB_PLATE, pubRevealed);
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, draftRevealed);
 codereviews.registerActivityListener(CR_ActivityType.DISCARD_DRAFT_COMMENT, draftDestroyed);
 
 
 
 
 
 
 
 var initialized = true;
 reloadCursors();
 }
 window.onload = function() {keysOnLoadHandler(); revsOnLoadHandler();};

</script>
<script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/8599073060794244502/js/dit_scripts.js"></script>

 
 
 
 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/8599073060794244502/js/ph_core.js"></script>
 
 
 
 
</div> 

<div id="footer" dir="ltr">
 <div class="text">
 <a href="/projecthosting/terms.html">Terms</a> -
 <a href="http://www.google.com/privacy.html">Privacy</a> -
 <a href="/p/support/">Project Hosting Help</a>
 </div>
</div>
 <div class="hostedBy" style="margin-top: -20px;">
 <span style="vertical-align: top;">Powered by <a href="http://code.google.com/projecthosting/">Google Project Hosting</a></span>
 </div>

 
 


 
 </body>
</html>

