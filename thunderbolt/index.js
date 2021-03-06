var mqtt = require('mqtt')
var client  = mqtt.connect('mqtt://mqtt.eclipse.org')

var ThunderboardReact = require('node-thunderboard-react');
var thunder = new ThunderboardReact();
let count = 0;
client.on('connect', () => {
    client.subscribe('dsei2400/santosh')
})

client.on('message',(topic,message)=>{
	if (topic==='dsei2400/santosh'){
		console.log(message.toString() )
	}
})

//')
  //  console.log(`Connected to MQTT Mosquitto`)
    // const publish = setInterval(() => {
    //     ++count;
    //     client.publish('testchannel/test', JSON.stringify({name: 'santosh', lastname: 'suwal', count}))
    //     // if (count >= 10) {
    //     //     clearInterval(publish);
    //     //     process.exit(0);
    //     // }
    // }, 5000);
//})

// Initialize the ThunderboardReact object
thunder.init((error) => {
  // Discover the Thunderboard React Board Kit
  thunder.startDiscovery((device) => {
    console.log('- Found ' + device.localName);
    // Stop the discovery process
    thunder.stopDiscovery();
    // Connect to the found device
    device.on('connect', _ => {
      console.log(`Device Connected`);
    })
    device.connect((err) => {
        if (err) {
            console.error(err)
        }
      console.log('- Connected ' + device.localName);
      // Get the sensored data
      getEnvironmentalSensing(device);
      setInterval(() => {
        getEnvironmentalSensing(device);
      }, 10000)
    });
  });
});

// Get the sensored data
function getEnvironmentalSensing(device) {
  device.getEnvironmentalSensing((error, res) => {
    // Show the data
    client.publish('dsei2400/adomakor412', JSON.stringify({
        ...res,
        latitude: '40.864946',
        longitude: '-73.9249753'
    }))
    
    console.log(`- Date: ${new Date()}`)
    console.log('Longitude: -73.9249753, Latitude: 40.864946');
    console.log('- Sensored data:');
    console.log('  - Humidity    : ' + res.humidity + ' %');
    console.log('  - Temperature : ' + res.temperature + ' °C');
    console.log('  - UV Index    : ' + res.uvIndex);
    console.log('  - Pressure    : ' + res.pressure + ' mbar');
    console.log('  - Light       : ' + res.light + ' lx');
    console.log('  - Sound       : ' + res.sound + ' dB');
  });
}
