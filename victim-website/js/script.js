function hidePremiumContent() {
    // Check if user has access to premium content
    console.log("Checking premium ... ");
    // ...
    
    console.log("User has no access - hiding content");
    var premiumContentElement = document.querySelector(".premiumContent");
    premiumContentElement.style.display = "none";

    var buyPremiumBanner = document.querySelector(".premiumBanner");
    buyPremiumBanner.style.display = "block";
}

document.onload = hidePremiumContent();