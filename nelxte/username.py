# --- Metadata ---#

__author__ = ["keouck", "parzival"]
__license__ = "MIT License"
__version__ = "1.0"
__maintainer__ = ["keouck", "parzival"]
__email__ = ["imerminu@tutanota.com", "suryakiranpradosh@gmail.com"]
__status__ = "Production"


# -- check_username -- #
def check_username(
    username: str, min_length: int = 2, max_length: int = 256, check_inappropriate: bool = True,  # noqa : E501
    check_length: bool = True
):
    if check_length:
        # -- checking if name is too short -- #
        if len(username) <= min_length:
            return (f"the username, {username} (length is {len(username)}), is"
                    f" too small(min length = {min_length})")
        # -- checking if name is too long -- #
        elif len(username) >= max_length:
            return (f"the username, {username} (length is {len(username)}), is"
                    f" too large(max length = {max_length})")
    if check_inappropriate:
        # -- List of inappropriate words -- #
        inappropriate_names = """anal,anus,arse,ass,ballsack,balls,bastard,bitch,biatch,bloody,blowjob,blow job,bollock,bollok,boner,boob,bugger,bum,butt,buttplug,clitoris,cock,coon,crap,cunt,damn,dick,dildo,dyke,fag,feck,fellate,fellatio,felching,fuck,f u c k,fudgepacker,fudge packer,flange,Goddamn,God damn,hell,homo,jerk,jizz,knobend,knob end,labia,lmao,lmfao,muff,nigger,nigga,omg,penis,piss,poop,prick,pube,pussy,queer,scrotum,sex,shit,s hit,sh1t,slut,smegma,spunk,tit,tosser,turd,twat,vagina,wank,whore,wtf""".lower().split(",")  # noqa : E501
        for i in inappropriate_names:
            if i in username:
                # -- triggered when inappropriate word is found -- #
                return (f"Inappropriate word : {i} (and possibly"
                        " more) detected in name")
    return "OK"
