var user= prompt('You meet a HANDSOME DRAGON! What do you do? FIGHT, SMOOCH, or RUN?').toUpperCase();
switch(user){
    case 'FIGHT':
        var sord= prompt('Do you have a majick sword? Yes or No?').toUpperCase();
        if (sord==='YES'){
            if (Math.random() > 0.5) {
                console.log('You hit the dragon and made it cry. It flies away. I guess you win, asshole');
            }
            else{
                console.log('You miss! Good job! The dragon laughs at you and you return to the village a disgrace.');
            };
        }
        else {
            console.log('You lack a sword and attempt to punch the dragon. You bruise your knuckles on its hide. The dragon laughs at you and you return to the village a disgrace.');       
        };
         break;
         
    case 'SMOOCH':
        var mwah = prompt("You lean in for a kiss. It pulls you in close. Do the dragon's sharp fangs deter you from giving it a passionate smooch? Yes or No?").toUpperCase();
        if (mwah === 'YES') {
            console.log('The dragon is hurt and offended. It flies away. You never see it again. It doesnt return your calls. You return to the village a disgrace.');
        }
        else{
            console.log('You and the dragon share a long, romantic smooch. It carries you back to its cave. You do not return to your village. You never look back. You and the dragon are very happy together.');
        };
        break;
        
        
        
        case 'RUN':
        var gottaGoFast = prompt('You attempt to flee from the dragon. It chases after you. It is very fast. It is very handsome. You cannot outrun the dragon. What do you do? FIGHT or SMOOCH?').toUpperCase();
            switch(gottaGoFast){
            case 'FIGHT':
        var sord= prompt('Do you have a majick sword? Yes or No?').toUpperCase();
        if (sord==='YES'){
            if (Math.random() > 0.5) {
                console.log('You hit the dragon and made it cry. It flies away. I guess you win, asshole');
            }
            else{
                console.log('You miss! Good job! The dragon laughs at you and you return to the village a disgrace.');
            };
        }
        else {
            console.log('You lack a sword and attempt to punch the dragon. You bruise your knuckles on its hide. The dragon laughs at you and you return to the village a disgrace.');       
        };
         break;
         
    case 'SMOOCH':
        var mwah = prompt("You lean in for a kiss. It pulls you in close. Do the dragon's sharp fangs deter you from giving it a passionate smooch? Yes or No?").toUpperCase();
        if (mwah === 'YES') {
            console.log('The dragon is hurt and offended. It flies away. You never see it again. It doesnt return your calls. You return to the village a disgrace.');
        }
        else{
            console.log('You and the dragon share a long, romantic smooch. It carries you back to its cave. You do not return to your village. You never look back. You and the dragon are very happy together.');
        };
        break;
        };
        break;
        
        default:
        console.log('come on pick a real option');
        break;
};