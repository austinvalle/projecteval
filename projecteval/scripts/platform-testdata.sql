INSERT INTO platform(
            name, release_date, "desc", developer, manufacturer, cpu, 
            memory, graphics, storage, added_by, date_added, last_modified_by, 
            last_modified)
    VALUES ('Xbox One', '2013-11-22', 'The Xbox One was announced on May 21, 2013, and it is the successor to the Xbox 360 and the third console in the Xbox family of consoles. Moving away from the PowerPC based architecture used in the Xbox 360, the console features an AMD processor built around the x86-64 instruction set. The console places an increasing emphasis on entertainment and integration with the Kinect peripheral, offering the ability to use an existing set-top box to watch live television programming (augmented by an enhanced program guide with support for voice commands), a built-in Skype client, and improved second screen support. The console also provides new functionality for use in games, such as an expanded Xbox Live service, improved Kinect functionality, cloud computing, the ability to automatically record and share video highlights from gameplay, and integrated support for live streaming gameplay online.',
	    'Microsoft', 'Microsoft', 'Custom 1.75 GHz AMD 8 Core APU (2 Quad Core Jaguar Modules)', '8GB DDR3', 
            '853 MHz AMD Radeon GCN', 'Hard drive, 500GB', 'testadmin', current_timestamp,
            'testadmin', current_timestamp),
            
            ('Playstation 4','2013-11-15', 'The Playstation 4 is the successor to Sony''s Playstation 3 console. Moving away from the Cell architecture, the PlayStation 4 will be the first in the Sony series to feature compatibility with the x86 architecture, specifically x86-64, which is a widely used platform common in many modern PCs. The idea is to make video game development easier on the next-generation console, attracting a broader range of developers large and small. These changes highlight Sony''s effort to improve upon the lessons learned during the development, production and release of the PS3. Other notable hardware features of the PS4 include 8 GB of memory and a faster Blu-ray drive.',
            'Sony Computer Entertainment', 'Sony Computer Entertainment',
            'Semi-custom 8-core AMDx86-64 Jaguar', '8GB GDDR5',
            'Semi-custom AMD GCN Radeon', 'Hard drive, 500GB', 'testadmin', current_timestamp,
            'testadmin', current_timestamp),

            ('Wii U', '2012-11-18', 'Wii U is the next great gaming console from Nintendo and it redefines how you will play next. With its innovative Wii U GamePad controller, it will not only introduce entirely new ways to play games, it will also transform how you connect with friends and enjoy entertainment.',
            'Nintendo', 'Nintendo',
            'Tri Core, 3 GHz PowerPC-based 45nm CPU', '2GB RAM',
            'Custom 40nm AMD GPU with 32 MB embedded eDRAM', 'Flash memory, 32GB', 'testadmin', current_timestamp,
            'testadmin', current_timestamp);
