// priority: 0

const $SturdyBlock = Java.loadClass('net.minecraft.world.level.block.TintedGlassBlock')
const $Blocks = Java.loadClass('net.minecraft.world.level.block.Blocks')
const $BlockProperties = Java.loadClass('net.minecraft.world.level.block.state.BlockBehaviour$Properties')
const $BlockItem = Java.loadClass('net.minecraft.world.item.BlockItem')
const $ItemProperties = Java.loadClass('net.minecraft.world.item.Item$Properties')
// 1.20 removed Material — push reaction is now set directly on the properties
const $PushReaction = Java.loadClass('net.minecraft.world.level.material.PushReaction')

let /**@type {Internal.CustomBuilderObject} */ sturdyBlackstone
StartupEvents.registry('block', e => {
    e.createCustom('sturdy_blackstone', () => new $SturdyBlock($BlockProperties.of().pushReaction($PushReaction.BLOCK)))
    e.createCustom('sturdy_netherrack', () => new $SturdyBlock($BlockProperties.of().pushReaction($PushReaction.BLOCK)))
})
StartupEvents.registry('item', e => {
    e.createCustom('sturdy_blackstone', () => new $BlockItem(Block.getBlock("kubejs:sturdy_blackstone"), new $ItemProperties()))
    e.createCustom('sturdy_netherrack', () => new $BlockItem(Block.getBlock("kubejs:sturdy_netherrack"), new $ItemProperties()))
})