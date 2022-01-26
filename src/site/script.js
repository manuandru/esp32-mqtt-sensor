import * as MQTTConfig from './config.js';

const topic = 'bedroom/+';
const options = {
    // Clean session
    clean: true,
    connectTimeout: 4000,
    protocolVersion: 5,
    username: MQTTConfig.username,
    password: MQTTConfig.password,
}

const client  = mqtt.connect(`ws://${MQTTConfig.ip}:${MQTTConfig.port}`, options)
client.on('connect', function () {
    client.subscribe(topic);
});

client.on('message', handleData)

function handleData(topic, message) {
    const measure = topic.split('/')[1];
    $('#' + measure).text(message.toString() + (measure === 'temperature' ? ' °C' : ' %'));
}
