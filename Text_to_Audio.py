import gtts

#file = gtts.gTTS("I AM A HERO")
anthem = """ Oh, say can you see, by the dawn's early light,
What so proudly we hailed at the twilight's last gleaming,
Whose broad stripes and bright stars through the perilous fight,
O'er the ramparts we watched, were so gallantly streaming?
And the rocket's red glare, the bombs bursting in air,
Gave proof through the night that our flag was still there;
Oh, say does that star-spangled banner yet wave
O'er the land of the free and the home of the brave."""

file=gtts.gTTS(anthem)
file.save("American_Anthem.mp3")
